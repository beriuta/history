"""management URL Configuration

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
from applistion import views

urlpatterns = [
    # 登录
    url(r'^login/$', views.login),
    url(r'^/$', views.class_list),
    # 班级
    url(r'^class_list/$', views.class_list),
    url(r'^delete_class/$', views.delete_class),
    url(r'^add_class/$', views.add_class),
    url(r'^edit_class/$', views.edit_class),
    # 学生
    url(r'^student_list/$', views.student_list),
    url(r'^delete_student/$', views.delete_student),
    url(r'^add_student/$', views.add_student),
    url(r'^edit_student/$', views.edit_student),
    # 老师
    url(r'^teacher_list/$', views.teacher_list),
    url(r'^delete_teacher/$', views.delete_teacher),
    url(r'^add_teacher/$', views.add_teacher),
    url(r'^edit_teacher/$', views.edit_teacher),
]
