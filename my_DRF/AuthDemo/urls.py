from django.conf.urls import url,include
from AuthDemo import views
from django.contrib import admin

urlpatterns = [
    url(r'^auth/', views.AuthView.as_view()),
    url(r'^login/', views.LoginView.as_view()),
    url(r'^test/', views.TestView.as_view()),
    url(r'^permission/', views.PermissionView.as_view()),

]