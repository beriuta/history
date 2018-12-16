from django.conf.urls import url
from VersionDemo.views import DemoView

urlpatterns = [
    url(r'^demo/', DemoView.as_view()),
]
