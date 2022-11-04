from django.urls import path,include
from . import views

urlpatterns = [
    path("",views.index,name='index'),
    path('register/',views.UserRegister,name='register'),
    path('LoginPage/',views.LoginPage,name='loginpage'),
    path('LoginUser/',views.LoginUser,name='login')

]