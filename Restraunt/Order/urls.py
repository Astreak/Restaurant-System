from django.urls import path,include
from . import views
from django.contrib.auth.views import *
import os
from .models import *
urlpatterns=[
    path("",views.home,name="main-home"),
    path("info/",views.info,name="main-info"),
    path("register/",views.register,name="main-register"),
    path("login/",LoginView.as_view(template_name="Order/login.html"),name="main-login"),
    path("logout/",LogoutView.as_view(template_name="Order/logout.html")),
    path("secret/",views.employee,name="Employee"),
    path("monetary/",views.monetary,name="main-Money"),
    path('order/',views.order,name="order")
    
    
    
]