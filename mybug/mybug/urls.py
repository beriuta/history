"""mybug URL Configuration

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
from applition import views

urlpatterns = [
    url(r'^login/', views.login),
    url(r'^select_publisher/', views.select_publisher),
    url(r'^add_publisher/', views.add_publisher),
    url(r'^delete_publisher/', views.delete_publisher),
    url(r'^alter_publisher/', views.alter_publisher),
    url(r'^book_list/',views.book_list),
    url(r'^delete_book/', views.delete_book)
]
