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
from crm import views
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/', views.login),
    url(r'^reg/', views.reg),
    url(r'^index/', views.index),
    url(r'^customer_list/', views.CustomerListView.as_view()),  # 所有客户列表
    url(r'^my_customer/', views.CustomerListView.as_view()),  # 我的客户列表
    url(r'^reg2/', views.RegView.as_view()),
    # url(r'^add/', views.add_customer),
    # url(r'^edit/(\d+)/$', views.edit_customer),
    # ----------------把add跟edit放在一个视图函数里------------
    url(r'add/', views.customer),
    url(r'edit/(\d+)/$', views.customer),
    # --------------------沟通记录表-------------
    url(r'consult_record/$',views.consult_record_list),
    url(r'add_consult_record/$',views.consult_record),
    url(r'edit_consult_record/(\d+)$',views.consult_record),

]
