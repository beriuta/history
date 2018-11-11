"""myfood URL Configuration

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
    url(r'^login/$', views.login),
    # 出版社
    url(r'^publisher_list/$', views.publisher_list),
    url(r'^add_publisher/$', views.add_publisher),
    url(r'^delete_publisher/$', views.delete_publisher),
    url(r'^edit_publisher/$', views.edit_publisher),
    # 书籍
    url(r'^book_list/$', views.book_list),
    url(r'^delete_book/$', views.delete_book),
    url(r'^add_book/$', views.add_book),
    url(r'^edit_book/$', views.edit_book),
    # 作者
    url(r'^author_list/$', views.author_list),
    url(r'^delete_author/$', views.delete_author),
    url(r'^add_author/$', views.add_author),
    url(r'^edit_author/$', views.edit_author),

    # 测试
    url(r'^book/([0-9]{4})/$', views.c_book),  # book(request,2018)  位置传参
    url(r'^book/(?P<year>[0-9]{4})/$', views.c_book),  # book(request,year=2018)  关键字参数
    url(r'^blog/$',views.blog),
    url(r'^blog/(?P<num>/d+)/$',views.blog),

]
