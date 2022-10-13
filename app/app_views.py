from email import message
from tkinter.tix import Tree
from urllib import request, response
from wsgiref.util import request_uri
from django.shortcuts import render, redirect
import requests
from django.conf import settings
from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import logout
import json
from django.core.paginator import Paginator
import django_tables2 as dtable

url = settings.URL

# Create your views here.

def auth(request):
    if request.POST.get('hiddenRegisterValue', '')=='if_register':
        name = request.POST['txtRegisterName']
        email = request.POST['txtRegisterEmail']
        pas1 = request.POST['RegisterPassword']
        pas2 = request.POST['RegisterConfirmPassword']

        data = {
            'username':name,
            'email':email,
            'password':pas1,
        }

        if pas1==pas2:
            register_response = requests.post('{url}user/'.format(url=url), data=data)
            status_code_list = [200, 302, 201]
            if register_response.status_code in status_code_list:
                messages.success(request,'Succesfully user created!!!')
                return redirect('login')
            else:
                messages.error(request,'Failed!!!')
                return redirect('register')
    elif request.POST.get('hiddenLogin','')=='if_login':
        name = request.POST['txtUserName']
        pas = request.POST['loginPassword']

        data={
            'username':name,
            'password':pas,
        }
        login_response = requests.post('{url}login/'.format(url=url), data=data)
        print(login_response.text)
        status_code_list = [200, 302, 201]
        json_login_response = json.loads(login_response.text)
        
        
        if login_response.status_code in status_code_list:
            superuser = (json_login_response['superuser'])

            # /// -->  CONVERTING FUNCTION VALUES TO GLOBAL TO USE IN OUTSIDE FUNC::::
            knox_token =(json_login_response["token"])
            user_name = (json_login_response["username"])
            user_id = (json_login_response["user_id"])
            request.session['get_token'] = knox_token
            request.session['get_username'] =  user_name
            request.session['get_user_id'] =  user_id
            
            # //// ----> ADMIN REDIRECT STATEMENT::::
            true = True
            flase = False
            if superuser == true:
                messages.success(request, f'Welcome {user_name}!!!')
                return redirect('admin')

            else:
                messages.success(request, f'Hi {user_name}, welcome !!!')
                return redirect('postpage')
            
        # if login_response.status_code == 400:
        #     v = admin_redirect.get('non_field_errors')
        #     if v[0] == 'True':
        #         return render(request, 'admin_page.html') 
        #     else:
        #         return redirect('login')
        else:
            messages.error(request,'Login Failed!!!')
            return redirect('login')
    else:
        return render(request, 'login.html')

# @staff_member_required
# @login_required(login_url='login')
# @user_passes_test
def home(request):
    if request.POST.get('hiddenIfPost','')=='if_post':
        id = request.POST['hiddenUserId']
        name = request.POST['txtPostName']
        image = request.FILES.get('fileImage')
        desc = request.POST['txtDescription']
        session_user_id = request.session['get_user_id']
        session_token = request.session['get_token']
        session_username = request.session['get_username']

        data = {
            'user_id':session_user_id,
            'post_name':name,
            'description':desc,
        }
        file ={
            'image':image,
        }
        try:
            header={'Authorization':'Token {toki}'.format(toki=session_token)}
            post_response = requests.post('{url}post/'.format(url=url), data=data, files=file, headers=header)
            status_code_list = [200, 302, 201]
            if post_response.status_code in status_code_list:
                messages.success(request, f'Successfully Logged In!!!')
                return redirect('postpage')
            else:
                messages.error(request,'Failed!!!')
                return redirect('postpage')
        except:
            return redirect('login')
    else:
        return redirect('postpage')        

# @login_required(login_url='login')
def approve_reject(request, id):
    if request.POST.get('hiddenApprove','')=='Approved':
        try:
            session_token = request.session['get_token']
            header={"Content-Type":"application/json; charset=UTF-8", 'Authorization':'Token {toki}'.format(toki=session_token)}
            update_get_response = requests.get('{url}post/{pk}/'.format(url=url, pk=id), headers=header)
            txt_val = update_get_response.text
            json_val = json.loads(txt_val)
            value = request.POST['hiddenApprove']
            data={
                'post_id':json_val['post_id'],
                'user_id':json_val['user_id'],
                'post_name':json_val['post_name'],
                'description':json_val['description'],
                'date':json_val['date'],
                'status': value,
            }
            approve_post_response = requests.put('{url}post/{pk}/'.format(url=url, pk=id), data=data)
            status_code_list = [200, 302, 201]
            if approve_post_response.status_code in status_code_list:
                messages.success(request, f'Successfully Approved!!!')
                return redirect('admin')
            else:
                messages.error(request,'Approval Failed!!!')
                return redirect('admin')
        except:
            return redirect('login')
    elif request.POST.get('hiddenReject','')=='Rejected':
        try:
            session_token = request.session['get_token']
            header={"Content-Type":"application/json; charset=UTF-8", 'Authorization':'Token {toki}'.format(toki=session_token)}
            reject_get_response = requests.get('{url}post/{pk}/'.format(url=url, pk=id))
            text_val = reject_get_response.text
            json_value = json.loads(text_val)
            value = request.POST['hiddenReject']
            reason = request.POST['txtReason']
            data={
                'post_id':json_value['post_id'],
                'user_id':json_value['user_id'],
                'post_name':json_value['post_name'],
                'description':json_value['description'],
                'date':json_value['date'],
                'status': value,
                'reason': reason,
            }
            reject_post_response = requests.put('{url}post/{pk}/'.format(url=url, pk=id), data=data)
            status_code_list = [200, 302, 201]
            if reject_post_response.status_code in status_code_list:
                messages.success(request, f'Successfully Approved!!!')
                return redirect('admin')
            else:
                messages.error(request,'Approval Failed!!!')
                return redirect('admin')
        except:
            return redirect('login')        
    else:
        return redirect('admin')

# @login_required(login_url='login')
def postpages(request):
    # GETTING GLOBAL VALUE FROM ANOTHER FUNCTION
    try:
        session_user_id = request.session['get_user_id']
        session_token = request.session['get_token']
        session_username = request.session['get_username']
        print(session_username)

        main_data = {
            'token':session_token,
            'username':session_username,
            'user_id':session_user_id,
        }
        header={"Content-Type":"application/json; charset=UTF-8", 'Authorization':'Token {toki}'.format(toki=session_token)}
        whole_data = requests.get('{url}wholedata/{pk}/'.format(url=url, pk=session_user_id), headers=header).json()
        return render(request, 'home.html',{'login_response':main_data, 'whole_data':whole_data})
    except:
        return redirect('login') 

def register(request):
    return render(request, 'register.html')

# @login_required(login_url='login')
def adminpages(request):
    try:
        session_token = request.session['get_token']
        header={"Content-Type":"application/json; charset=UTF-8", 'Authorization':'Token {toki}'.format(toki=session_token)}
        admin_table = requests.get('{url}admintable/'.format(url=url), headers=header).json()
        admin_table_foot = requests.get('{url}admintablefoot/'.format(url=url), headers=header).json()
        return render(request, 'admin_page.html', {'admin_table':admin_table, 'admin_table_foot':admin_table_foot})
    except:
        return redirect('login')

# @login_required(login_url='login')
def signout(request):
    try:
        session_token = request.session['get_token']
        header={"Content-Type":"application/json; charset=UTF-8", 'Authorization':'Token {toki}'.format(toki=session_token)}
        logout_reponse = requests.post('{url}logout/'.format(url=url), headers=header)
        logout(request)
        messages.error(request,("Logged out successfully!!!!")) 
        return redirect('login')
    except:
        return redirect('login')
    

# @login_required(login_url='login')
def feedpages(request):
    try:
        session_token = request.session['get_token']
        header={"Content-Type":"application/json; charset=UTF-8", 'Authorization':'Token {toki}'.format(toki=session_token)}
        data = requests.get('{url}approvefeed/'.format(url=url), headers=header).json()
        paginator_data = Paginator(data, 10)
        print(paginator_data)
        page_number = request.GET.get('page')
        page_obj = paginator_data.get_page(page_number)
        return render(request, 'feed.html', {'data':page_obj})
    except:
        return redirect('login')

def adminpage2(request):
    session_token = request.session['get_token']
    # if request.GET.get('showEntries') == True:
    # if request.GET.get('showEntries') != None:
    try:
        header={"Content-Type":"application/json; charset=UTF-8", 'Authorization':'Token {toki}'.format(toki=session_token)}
        admin_table = requests.get('{url}admintable/'.format(url=url), headers=header).json()
        Page_data = requests.get('{url}admintablefoot/'.format(url=url), headers=header).json()
        if request.GET.get('showEntries', ''):
            val = request.GET.get('showEntries')
            print(val)
            admin_table_foot = Paginator(Page_data, val)
            page_number = request.GET.get('page')
            page_obj = admin_table_foot.get_page(page_number)
            return render(request, 'admin_page-2.html', {'admin_table':admin_table, 'admin_table_foot':page_obj})
        else:
            admin_table_foot = Paginator(Page_data, 5)
            page_number = request.GET.get('page')
            page_obj = admin_table_foot.get_page(page_number)
            return render(request, 'admin_page-2.html', {'admin_table':admin_table, 'admin_table_foot':page_obj})
    except:
        return redirect('login')
    # else:
    #     header={"Content-Type":"application/json; charset=UTF-8", 'Authorization':'Token {toki}'.format(toki=session_token)}
    #     admin_table = requests.get('{url}admintable/'.format(url=url), headers=header).json()
    #     admin_table_foot = Paginator(requests.get('{url}admintablefoot/'.format(url=url), headers=header).json(), 7)
    #     page_number = request.GET.get('page')
    #     page_obj = admin_table_foot.get_page(page_number)
    #     return render(request, 'admin_page-2.html', {'admin_table':admin_table, 'admin_table_foot':page_obj})
 
