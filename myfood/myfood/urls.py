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
from django.conf.urls import url,include
from django.contrib import admin
from applistion import views
from app01 import urls as app01_urls
from app02 import urls as app02_urls

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

    # 把所有以app01开头的都交给app01.urls去处理
    url(r'^app01/', include('app01.urls',namespace='app01')),  # url不能以$结尾
    # 把所有以app02开头的都交给app02.urls去处理
    url(r'^app02/', include('app02.urls',namespace='app02'))


]
