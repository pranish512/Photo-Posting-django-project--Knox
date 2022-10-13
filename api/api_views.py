from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from .models import PostModel
from .serializer import *
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status

from django.contrib.auth import login

from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as LoginViewKnox
from knox.auth import TokenAuthentication
from django.contrib.auth.models import User

from django_tables2 import RequestConfig
from django.template import RequestContext
from django.views.generic.base import TemplateView

# Create your views here.

# NEST API DATA:::::
class CreateUserGenerics(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = CreateUserSerializer

class NestPostGenerics(generics.ListCreateAPIView):
    queryset = PostModel.objects.all()
    serializer_class = NestPostSerializer

# DATA POSTING API'S
class PostUserGenerics(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = PostUserSerializer

class EditUserGenerics(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = PostUserSerializer

class PostPostGenerics(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated, )
    queryset = PostModel.objects.all()
    serializer_class = PostPostSerializer

class EditPostGenerics(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated, )
    queryset = PostModel.objects.all()
    serializer_class = PostPostSerializer

class LoginView(LoginViewKnox):
    # authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.AllowAny,) #IsAuthenticated

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data) #KnoxTokenSerializer
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        if request.user.is_superuser:
            return super(LoginView, self).post(request, format=None)
        return super(LoginView, self).post(request, format=None)

class EntryPermissionGenerics(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = EntryPermissionSerializer

class NestUserPostGenerics(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = NestUserPostSerializer

class EditUserPostGenerics(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = NestUserPostSerializer


# FILTERED DATA API's
class AdminTableGenerics(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAdminUser,)
    queryset = PostModel.objects.filter(status__isnull=True).all()
    serializer_class = PostPostSerializer

class AdminTableStatusAssignedGenerics(generics.ListCreateAPIView):
    # permission_classes = (permissions.IsAdminUser,)
    # filter(status__isnull=True).all()
    queryset = PostModel.objects.exclude(status__isnull=True).all()
    serializer_class = PostPostSerializer

class ApprovedFeedGenerics(generics.ListCreateAPIView):
    reject = 'Approved'
    permission_classes = (permissions.IsAuthenticated,)
    queryset = PostModel.objects.filter(status=reject).all()
    serializer_class = ApprovePostSerializer

class RejectedFeedGenerics(generics.ListCreateAPIView):
    reject = 'Rejected'
    permission_classes = (permissions.IsAuthenticated,)
    queryset = PostModel.objects.filter(status=reject).all()
    serializer_class = PostPostSerializer

# POST DATA ISIDE THE USER DATA::::
class WholeDataGenerics(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = WholeDataSerializer

class EditWholeDataGenerics(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = WholeDataSerializer

class AdminView(TemplateView):
     def get(self, request, *args, **kwargs):
         data = PostModel.objects.exclude(status__isnull=True).all()
         context = self.get_context_data(**kwargs)
         context['table'] = data
         return self.render_to_response(context)

# def plyn(request):
#     table = PostModel(PostModel.objects.all())
#     RequestConfig(request).configure(table)
#     return render(request, 'plyn.html', {'table': table})
#    return render_to_response('plyn.html', {"records": table,}, context_instance=RequestContext(request))