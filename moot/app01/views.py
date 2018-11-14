from django.shortcuts import render,HttpResponse
from django import views
from app01.models import UserInfo
from django.http import JsonResponse
# Create your views here.


def login(request):
    if request.method == 'POST':
        user = request.POST.get('user')
        pwd = request.POST.get('pwd')
        # return HttpResponse('登录成功')
        print(user)
        print(pwd)
        res = {'code': 0}  # 定义一个res
        ret = UserInfo.objects.filter(username=user, password=pwd)
        if ret:
            res['next_url'] = '/index/'
            return JsonResponse(res)  # 把res传入前端页面
        else:
            res['code'] = 1
            res['msg_error'] = '用户名或密码输入错误'
            return JsonResponse(res)
    return render(request, 'login.html')


class indexView(views.View):
    def get(self,request):
        return render(request,'index.html')


def upload(request):
    if request.method == 'POST':
        file_obj = request.FILES.get('xx')
        file_name = file_obj.name
        with open(file_name,  'wb') as f:
            for c in file_obj.chunks():
                f.write(c)
        return HttpResponse('上传成功！')

    return render(request, 'upload.html')