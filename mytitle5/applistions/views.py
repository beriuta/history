"""
此文件包含cookie版七天免登陆
使用装饰器做cookie版登录验证
以及csrf_exempt:装饰的视图不需要验证csrftoken
以及csrf_protect:装饰的视图必须要验证csrftoken
60秒内限制访问频率小于三次
"""
from django.shortcuts import render, HttpResponse, redirect
from django.views.decorators.csrf import csrf_exempt,csrf_protect
from django.utils.decorators import method_decorator
from applistions.models import UserInfo
from functools import wraps
from django import views


# 使用装饰器做cookie版的登录验证
def check_login(func):
    @wraps(func)
    def inner(request, *args, **kwargs):
        # 先做cookie验证
        session_user = request.session.get('user', None)
        # 从cookie中取得随机字符串
        # 解密并反序列化session_data,得到一个大字典
        # 从大字典中根据key取值
        if session_user:
            rep = func(request, *args, **kwargs)
            # 如果获取到了字符串,说明用户已经登陆过了,那么就根据用户登录的网址获取到相应的视图函数
            # 之后返回这个视图函数的返回值
            return rep
        else:
            next_url = request.path_info
            return redirect('/login/?nextUrl={}'.format(next_url))

    return inner


# Create your views here.
# 登录CBV版,实现七天免登陆
class LoginView(views.View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        name = request.POST.get('user')
        pwd = request.POST.get('pwd')
        remember = request.POST.get('remember', None)
        user_obj = UserInfo.objects.filter(username=name, password=pwd).first()
        if user_obj:
            # 添加session
            next_url = request.GET.get('nexUrl', '/home/')
            # 登陆成功之后查看有没有用户想要进入的页面,如果没有,默认进入home页面
            request.session['user'] = user_obj.id
            request.session['hobby'] = 'eat'
            request.session['age'] = '8000'
            # 如果勾选了7天免登陆
            if remember:
                request.session.set_expiry(7*24*60*60)
            else:
                request.session.set_expiry(0)  # 关闭浏览器就失效
            return redirect(next_url)
        else:
            return render(request, 'login.html', {'error_msg': '用户名或密码输入错误'})


# 首页
@check_login
def home(request):
    return HttpResponse('登陆成功')


# 主页
# @method_decorator(check_login,name='get')  # 或者可以写到dispatch上面,不需要写name属性
class IndexView(views.View):
    # @method_decorator(csrf_exempt)
    # def dispatch(self, request, *args, **kwargs):
    #     return super(IndexView,self).dispatch(request,*args,**kwargs)
    #
    # def get(self, request):
    #     return render(request, 'index.html')
    pass


# 注销
@check_login
def logout(request):
    # 删除当前的session并让cookie失效
    request.session.flush()
    return redirect('/login/')


