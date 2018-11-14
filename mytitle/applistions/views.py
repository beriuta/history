from django.shortcuts import render, redirect, HttpResponse
from applistions.models import Publisher, UserInfo
from django.utils.decorators import method_decorator  # 把装饰函数的装饰器包装成可以装饰类中方法的装饰器
from django.views import View
from django.http import JsonResponse
from functools import wraps


# Create your views here.
# def check_login(func):
#     @wraps(func)
#     def inner(request,*args,**kwargs):
#         # 先做Cookie验证
#         # cookie_value = request.COOKIES.get('h1')  # 包含所有cookie的字典。 键和值是字符串。
#         cookie_value = request.get_signed_cookie(key='key', salt='shenjingbing', default=None)
#         if cookie_value == 'value':
#             rep = func(request, *args, **kwargs)
#             return rep
#         else:
#             return_url = request.path_info  # 拿到当前请求的URL
#             return redirect('/login/?returnUrl={}'.format(return_url))
#     return inner
#
#
# # 登录
# class LoginViwe(View):
#     def get(self, request):
#         return render(request, 'login.html')
#
#     def post(self, request):
#         # 获取post的user,password
#         user = request.POST.get('user')
#         pwd = request.POST.get('pwd')
#         print(user)
#         print(pwd)
#         # 如果成功，就return下一个url
#
#         if UserInfo.objects.filter(name=user,password=pwd):
#             print(request.get_full_path())
#             next_url = request.POST.get('returnUrl', '/index/')
#             print(next_url)
#             print('-'*120)
#             rep = redirect(next_url)  # 这里一个错误，跳转redirect写成了render
#             # rep.set_cookie('hl', 'dsb', max_age=7 * 24 * 60 * 60)  # 七天免登陆，告诉浏览器在自己本地保存一个键值对 hl: dsb
#             rep.set_signed_cookie('key', 'value', salt='shenjingbing', max_age=7*24*60*60)
#             return rep
#
#         # 否则就返回一个错误信息
#         return render(request, 'login.html', {'error_msg': '用户名或密码输入错误！'})


# Session跟cookie一起
def check_login(func):
    @wraps(func)
    def inner(request, *args, **kwargs):
        # 先做Cookie验证
        # cookie_value = request.COOKIES.get('h1')  # 包含所有cookie的字典。 键和值是字符串。
        session_value = request.session.get('user', None)
        print(session_value)
        if session_value:
            rep = func(request, *args, **kwargs)
            return rep
        else:
            return_url = request.path_info  # 拿到当前请求的URL
            return redirect('/login/?returnUrl={}'.format(return_url))

    return inner


# 登录
class LoginViwe(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        # 获取post的user,password
        user = request.POST.get('user')
        pwd = request.POST.get('pwd')
        remember = request.POST.get('remember', None)
        print(user)
        print(pwd)
        # 如果成功，就return下一个url
        user_obj = UserInfo.objects.filter(name=user, password=pwd).first()
        print(user_obj.name)
        if user_obj:
            print(request.get_full_path())
            next_url = request.POST.get('returnUrl', '/index/')
            print(next_url)
            print('-' * 120)
            request.session['user'] = user_obj.name
            request.session['hobby'] = '吃'
            request.session['age'] = 32
            if remember:
                request.session.set_expiry(7 * 24 * 60 * 60)
            else:
                request.session.set_expiry(0)
            return redirect(next_url)
        # 否则就返回一个错误信息
        else:
            return render(request, 'login.html', {'error_msg': '用户名或密码输入错误！'})


@check_login
def index(request):
    data = Publisher.objects.all()
    return render(request, 'index.html', {'publisher_list': data})


def delete_publisher(request):
    if request.method == 'POST':
        delete_id = request.POST.get('id')
        print(delete_id)
        res = {'code': 0}
        try:
            Publisher.objects.filter(id=delete_id).delete()
            print('要删除了！')
        except Exception as a:
            res['code'] = 1
            res['error_msg'] = str(a)
        return JsonResponse(res)


@check_login
def home(request):
    return HttpResponse('home!')


# @method_decorator(check_login, name='get')
class UserInfoView(View):
    @method_decorator(check_login)
    def dispatch(self, request, *args, **kwargs):
        return super(UserInfoView, self).dispatch(self, *args, **kwargs)

    def get(self, request):
        return render(request, 'xxx.html')
