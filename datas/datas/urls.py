"""datas URL Configuration

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
from applstion import views

urlpatterns = [
    # 登录的URL
    url(r'^login/$',views.login),
    # 出版社增删改查的URL
    url(r'^publisher_list/$',views.publisher_list),
    url(r'^add_publisher/$',views.add_publisher),
    url(r'^delete_publisher/$',views.delete_publisher),
    url(r'^edit_publisher/$',views.edit_publisher),
    url(r'^edit_publisher/$',views.edit_publisher),
    # 书籍表格关联出版社的增删改查
    url(r'^add_book/$',views.add_book),
    url(r'^delete_book/$',views.delete_book),
    url(r'^edit_book/$',views.edit_book),
    url(r'^select_book/$',views.select_book),
]
