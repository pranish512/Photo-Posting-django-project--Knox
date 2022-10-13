from unicodedata import name
from django.urls import path
from . import app_views as views
from .app_views import *

urlpatterns = [
    path('home/', views.home, name='home'),
    path('login/', views.auth, name='login'), 
    path('logout/', views.signout, name='logout'), 
    path('register/', views.register, name='register'),
    path('approvereject/<int:id>/',views.approve_reject, name='approvereject'),
    path('', views.postpages, name='postpage'),
    path('adminpage/', views.adminpages, name='admin'),
    path('feed/', views.feedpages, name='feed'),
    path('adminpage2/', views.adminpage2, name="adminpage2"),
]