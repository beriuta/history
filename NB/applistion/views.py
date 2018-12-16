from django.shortcuts import render
from applistion import models
import datetime
import time
from django.views.decorators.cache import cache_page

# Create your views here.


# @cache_page(5)  # 加了一个缓存,每五秒重新到数据库中获取新的内容
def user_list(request):
    print('要获取新的内容了')
    ret = models.User.objects.all()
    now = time.time()
    return render(request,'user_list.html',{'user_list':ret,'now':now})