from django.conf.urls import url
from SerDemo import views
from django.contrib import admin
from rest_framework.routers import DefaultRouter

# 第一步实例化对象
router = DefaultRouter()

# 第二步,把路由以及视图注册
router.register('list',views.BookModelView)

urlpatterns = [
    # # url(r'^book/', views.BookView.as_view()),
    # url(r'^list/', views.BookModelView.as_view({"get": "list", "post": "create"})),
    # # url(r'^retrieve/(?P<id>\d+)/$', views.BookEditView.as_view()),
    # url(r'^retrieve/(?P<pk>\d+)/$',
    #     views.BookModelView.as_view({"get": "retrieve", "put": "update", "delete": "destroy"})),
]


# 把生成好的路由注册进去
urlpatterns += router.urls