from django.urls import path
from . import views

urlpatterns = [ 
    path('', views.index, name='index'),
    path('signUp/', views.signUp, name='signUp'),
    path('signIn/', views.signIn, name='signIn'),
    path('userProfile/', views.userProfile, name='userProfile'),
    path('userEditProfile/', views.userEditProfile, name='userEditProfile'),
    path('reviewDashboard/', views.reviewDashboard, name='reviewDashboard'),
    path('reviewEdit/', views.reviewEdit, name='reviewEdit'),
    path('reviewDelete/', views.reviewDelete, name='reviewDelete'),
    path('logOut/', views.logOut, name='logOut')
]