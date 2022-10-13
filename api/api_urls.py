from django.urls import path
from . import api_views as views
from knox.views import LogoutView as LogoutViewKnox
from .api_views import *

urlpatterns = [ 

    # LISTING NESTED DATA::::
    path('nestuser/', CreateUserGenerics.as_view()),
    path('nestpost/', NestPostGenerics.as_view()),

    # POST | UPDATE | DELATE::::
    path('user/', PostUserGenerics.as_view()),
    path('user/<int:pk>/', EditUserGenerics.as_view()),
    path('post/', PostPostGenerics.as_view()),
    path('post/<int:pk>/', EditPostGenerics.as_view()),

    # LOGIN URL::::
    path('login/', views.LoginView.as_view()),
    path('logout/', LogoutViewKnox.as_view()),
    path('entry/', EntryPermissionGenerics.as_view()),

    # USER POST NEST URL:::
    path('nestuserpost/', NestUserPostGenerics.as_view()),
    path('nestuserpost/<int:pk>/', EditUserPostGenerics.as_view()),

    path('admintable/', AdminTableGenerics.as_view()),
    path('admintablefoot/', AdminTableStatusAssignedGenerics.as_view()),
    path('approvefeed/', ApprovedFeedGenerics.as_view()),
    path('rejectfeed/', RejectedFeedGenerics.as_view()),

    path('wholedata/', WholeDataGenerics.as_view()),
    path('wholedata/<int:pk>/', EditWholeDataGenerics.as_view()),
]
