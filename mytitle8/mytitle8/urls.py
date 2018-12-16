"""mytitle8 URL Configuration

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
from crm import views, ajax_views, head_teacher_views
from django.contrib import admin

urlpatterns = [
    url(r'^admin/$', admin.site.urls),
    url(r'^login/$', views.login),
    url(r'^reg/$', views.reg),
    url(r'^index/$', views.index),
    url(r'^customer_list/$', views.CustomerListView.as_view()),  # 所有客户列表
    url(r'^my_customer/$', views.CustomerListView.as_view()),  # 我的客户列表
    url(r'^reg2/$', views.RegView.as_view()),
    # url(r'^add/', views.add_customer),
    # url(r'^edit/(\d+)/$', views.edit_customer),

    # ----------------把add跟edit放在一个视图函数里------------
    url(r'^add/$', views.customer),
    url(r'^edit/(\d+)/$', views.customer),

    # --------------------沟通记录表-------------
    url(r'^consult_record/(?P<cid>\d+)/$', views.consult_record_list, name='consult_record'),
    url(r'^add_consult_record/$', views.consult_record),
    url(r'^edit_consult_record/(\d+)/$', views.consult_record),

    # ----------------------报名表-------------------
    url(r'^enrollment_list/(?P<customer_id>\d+)/$', views.EnrollmentListView.as_view(), name='enrollment_list'),
    # 查看报名记录
    url(r'^add_enrollment/(?P<customer_id>\d+)/$', views.enrollment),
    url(r'^edit_enrollment/(?P<enrollment_id>\d+)/$', views.enrollment),

    # AJAX提交
    url(r'^ajax_class/$', ajax_views.ajax_class),

    # 班级管理
    url(r'^class_list/$', head_teacher_views.ClassListView.as_view()),
    url(r'add_class/$', head_teacher_views.op_class),
    url(r'edit_class/$', head_teacher_views.op_class),

    # 课程记录
    # 因为查询课程记录 一定要指定查询某个班级的上课记录
    url(r'course_record_list/(?P<class_id>\d+)$', head_teacher_views.CourseListView.as_view(), name='course_record_list'),
    url(r'add_course_record/(?P<class_id>\d+)$', head_teacher_views.course_record, name='add_course_record'),
    url(r'edit_course_record/(?P<course_record_id>\d+)$', head_teacher_views.course_record, name='edit_course_record'),

    # 学习记录
    url(r'^study_record_list/(?P<course_record_id>\d+)/$',head_teacher_views.study_record_list,name='study_record_list')
]
