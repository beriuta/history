from django.shortcuts import render, redirect, HttpResponse
from django.http import HttpResponse
from applistion.models import UserInfo
from django.utils.decorators import method_decorator
from django import views
import datetime
import time


# Create your views here.
class LoginView(views.View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        username = request.POST.get('name')
        pwd = request.POST.get('pwd')
        ret = UserInfo.objects.filter(username=username, password=pwd)
        if ret:
            return HttpResponse('登录成功！')
        return render(request, 'login.html')


class UploadView(views.View):
    def get(self, request):
        return render(request, 'upload.html')

    def post(self, request):
        print(request.POST)
        print(request.FILES)
        print(request.FILES.get('filename'), type(request.FILES.get('filename')))
        filename_obj = request.FILES.get('filename')
        filename = filename_obj.name
        print(filename)
        with open(filename, 'wb') as f:
            for i in filename_obj.chunks():
                f.write(i)
        return HttpResponse('收到了！')


def current_datetime(requeast):
    now = datetime.datetime.now()
    html = '<html><body>It is now {} </body></html>'.format(now)
    return HttpResponse(html)


# def add_class(request):
#     if request.method == 'POST':
#         ret = request.POST.get('name')
#         if ret == '一年三班':
#             return render(request, 'class_list.html')
#     return render(request, 'add_class.html')
class AddClass(views.View):
    def get(self, request):
        return render(request, 'add_class.html')

    def post(self, request):
        class_name = request.POST.get('class_name')
        if class_name == '一年八班':
            return render(request, 'class_list.html')


def wrapper(func):
    def inner(*args, **kwargs):
        start_time = time.time()
        ret = func(*args, **kwargs)
        end_time = time.time()
        print('used', end_time - start_time)
        return ret

    return inner


# @wrapper
# def add_class(request):
#     if request.method == 'POST':
#         class_name = request.POST.grt('class_name')
#         if class_name == '一年八班':
#             return render(request,'class_list.html')
#     return render(request,'add_class.html')

# class AddClass(views.View):
#     @method_decorator(wrapper)
#     def get(self, request):
#         return render(request, 'add_class.html')
#
#     def post(self, request):
#         class_name = request.POST.get('class_name')
#         if class_name == '一年三班':
#             return render(request, 'class_list.html')


def upload(request):
    """
    保存上传文件钱，数据需要存放在某个位置，默认当上传文件小于2.5m时，Django会将上传文件的全部内容镀金内存
    从内存读取一次，写磁盘一次
    但当上传文件很大时，Django会把上传我文件写到临时文件中，然后存放到系统历史文件夹中
    :param request:
    :return:
    """
    if request.method == 'POST':
        # 从请求的FILES中获取上传文件的文件名，file为页面上type=files类型input的name属性
        filename = request.FILES['filename'].name
        # 在项目目录下新建一个文件
        with open(filename, 'wb') as f:
            # 从上传的文件对象中一点一点读
            for chunk in request.FILES['filename'].chunks():
                # 写入本地文件
                f.write(chunk)
        return HttpResponse('上传成功！')
    return render(request, 'upload.html')
