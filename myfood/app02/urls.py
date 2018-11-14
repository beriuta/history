from django.conf.urls import url
from app02 import views

# 测试
urlpatterns = [
    url(r'^index/$',views.index),
    url(r'^login/$',views.login)
]