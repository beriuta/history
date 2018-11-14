from django.conf.urls import url
from app01 import views

# 测试
urlpatterns = [
    # url(r'^book/([0-9]{4})/$', views.c_book),  # book(request,2018)  位置传参
    url(r'^bookvygt/', views.book, name='xxx'),  # book(request,2018)  位置传参
    # url(r'^book/(?P<year>[0-9]{4})/$', views.c_book),  # book(request,year=2018)  关键字参数
    # url(r'^book/(?P<year>[0-9]{4})/$', views.c_book, {'author': '席爱香'}),  # book(request,year=2018)  关键字参数
    url(r'^blog/$', views.blog, ),
    # url(r'^blog/(?P<num>\d+)/$', views.blog),
    url(r'^book/$',views.book),
    url(r'^book_list/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/$',views.book_list,name='book_list')
    ]