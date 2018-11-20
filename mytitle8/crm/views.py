from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from crm.forms import RegForm
from django.contrib import auth
from crm.models import UserProfile,Customer
from django import views


# Create your views here.
# 登录


def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        # print(email)

        pwd = request.POST.get('password')
        # print(pwd)
        is_remember = (request.POST.get('remember', None) == '777')
        user_obj = auth.authenticate(email=email, password=pwd)
        # print(user_obj)
        if user_obj:
            # 设置session
            auth.login(request, user_obj)
            if is_remember:
                request.session.set_expiry(7 * 24 * 60 * 60)
            else:
                request.session.set_expiry(0)
            return redirect('/index/')
        else:
            return render(request, 'login.html', {'error_msg': '邮箱或密码错误'})
    return render(request, 'login.html')


@login_required
def index(request):
    return HttpResponse('登陆成功!')


def reg(request):
    if request.method == 'POST':
        res = {'code': 0}
        forms_obj = RegForm(request.POST)
        # print(forms_obj)
        if forms_obj.is_valid():
            # email = request.POST.get('email')
            # print(email)
            forms_obj.cleaned_data.pop('re_password')
            # pwd = request.POST.get('password')
            ret = UserProfile.objects.create_user(**forms_obj.cleaned_data)
            # print(ret)
            res['url'] = '/login/'
            # return redirect('/login/')
        else:
            res['code'] = 1
            res['error_msg'] = forms_obj.errors
        return JsonResponse(res)
        # return render(request, 'reg.html', {'form': forms_obj})
    form_obj = RegForm()
    return render(request, 'reg.html', {'form': form_obj})


class RegView(views.View):

    def get(self,request):
        form_obj = RegForm()
        return render(request,'reg2.html',  {'form_obj': form_obj})

    def post(self,request):
        form_obj = RegForm(request.POST)
        if form_obj.is_valid():
            # 方法一:
            # 先把re_password字段去掉
            form_obj.cleaned_data.pop('re_password')
            # 去数据库创建新用户
            UserProfile.objects.create_user(**form_obj.cleaned_data)
            return redirect('/login/')
        return render(request,'reg2.html',{'form_obj': form_obj})


@login_required
def customer_list(request):
    data = Customer.objects.all()
    return render(request,'customer_list.html',{'customer_list':data})


def logout(request):
    auth.logout(request)
    return redirect('/login/')





