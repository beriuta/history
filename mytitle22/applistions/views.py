from django.shortcuts import render, redirect, HttpResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from applistions.models import UserInfo
from functools import wraps
from django.views import View


# Create your views here.


def coklin_login(func):
    @wraps(func)
    def inner(request, *args, **kwargs):
        session_user = request.session.get('name', None)
        if session_user:
            rep = func(request, *args, **kwargs)
            return rep
        else:
            return_url = request.path_info
            print(return_url)
            print('111')
            return redirect('/login/?Nexurl={}'.format(return_url))
    return inner


# @coklin_login  # 登录不能再包登录装饰器,不然会一直重定向,浏览器显示重定向的次数过多
def login(request):
    if request.method == 'POST':
        print(type(request))
        user = request.POST.get('user')
        pwd = request.POST.get('pwd')
        ret_obj = UserInfo.objects.filter(username=user, password=pwd).first()
        print(UserInfo.objects.filter(username=user, password=pwd))
        if ret_obj:
            request_url = request.GET.get('Nexurl', '/home/')
            print(request_url)
            request.session['name'] = ret_obj.username  # 这个地方不能直接用对象,JSON不能序列化对象
            request.session['age'] = 12
            request.session['hobby'] = '吃'
            return redirect(request_url)

    return render(request, 'login.html')


@coklin_login
def home(request):
    print('zzzz')
    return HttpResponse('这是home页面')


class FromView(View):
    @method_decorator(csrf_exempt)  # 保证所装饰的函数内容不受csrf的约束  csrf_protect :保证只有所装饰的函数受csrf的约束
    def dispatch(self, request, *args, **kwargs):
        return super(FromView,self).dispatch(request,*args,**kwargs)

    def get(self, request):
        print(request)
        return render(request, 'from.html')

    def post(self, request):
        ret = request. POST.get('user')
        print(ret)
        return HttpResponse('ok')
