"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.shortcuts import render,HttpResponse


def login(request):
    return render(request,'login.html')


def aler(request):
    email = request.POST.get('email',None)
    pwd = request.POST.get('pwd', None)
    print('-' * 120)
    if email == 'hanlei@123.com' and pwd == 'hanlei123':
        return HttpResponse('登陆成功')
    else:
        return HttpResponse('用户名或密码错误')


urlpatterns = [
    url(r'^login/', login),
    url(r'^aler/', aler)
]
