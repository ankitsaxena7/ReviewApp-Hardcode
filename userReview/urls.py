from django.urls import path
from . import views

urlpatterns = [ 
    path('', views.index, name='index'),
    path('signUp/', views.signUp, name='signUp'),
    path('signIn/', views.signIn, name='signIn'),
    path('userDashboard/', views.userDashboard, name='userDashboard'),
]