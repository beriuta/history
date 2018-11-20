from django.shortcuts import render,redirect,HttpResponse
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# 默认是auth的数据库,如果要修改,可以自定义添加字段,添加的类要继承AbstractUser父类


# Create your views here.
# 注册
def reg(request):
    if request.method == 'POST':
        user = request.POST.get('username')
        pwd = request.POST.get('password')
        el = request.POST.get('email')
        # 都经过有效性校验了
        # 去数据库更新一条记录
        # 创建普通用户
        # User.objects.create_user(username=user, password=pwd)
        # 创建超级用户,超级用户有权限登录auth后台
        User.objects.create_superuser(username=user, password=pwd, email=el)
        # 创建成功,跳转到登录页
        return redirect('/login/')  # 再登录一遍,获取到cookie字符串,方便以后登录校验身份
    return render(request, 'reg.html')


# 登录
def login(request):
    if request.method == 'POST':
        user = request.POST.get('username')
        pwd = request.POST.get('password')
        # 调用auth模块的认证方法判断用户名和密码是否正确,正确返回一个user_obj
        user_obj = auth.authenticate(username=user, password=pwd)
        if user_obj:
            # 登陆成功,把当前登录的用户id保存在session中
            auth.login(request, user_obj)
            return redirect('/index/')
        else:
            return render(request, 'login.html', {'error_msg': '用户名或密码错误'})
    print(type(request))
    return render(request, 'login.html')


# 注销
def logout(request):
    auth.logout(request)
    return redirect('/login/')


# 修改密码
def change_pwd(request):
    # 验证原密码是否正确
    if request.method == 'POST':
        # user = request.method.get('username')
        old_password = request.POST.get('password')
        # print(request.user,type(request.user))
        is_ok = request.user.check_password(old_password,)
        if is_ok:
            # 修改密码
            new_pwd = request.POST.get('new_password')
            request.user.set_password(new_pwd)
            request.user.save()
            return redirect('/login/')
    return render(request, 'change_pwd.html')


# 登陆成功跳转的页面
@login_required
def index(request):
    return render(request,'index.html')