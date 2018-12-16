from django.conf.urls import url
from applistions import views

urlpatterns = [
    url(r'^list$',views.TeacherView.as_view()),
    url(r'^list2$',views.StudentView.as_view()),

]