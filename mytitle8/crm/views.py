from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from crm.forms2 import RegForm, CustomerForm
from django.contrib import auth
from crm.models import UserProfile, Customer
from django import views
from utils.mypage import Pagination


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
            return redirect('/customer_list/')
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

    def get(self, request):
        form_obj = RegForm()
        return render(request, 'reg2.html', {'form_obj': form_obj})

    def post(self, request):
        form_obj = RegForm(request.POST)
        if form_obj.is_valid():
            # 方法一:
            # 先把re_password字段去掉
            form_obj.cleaned_data.pop('re_password')
            # 去数据库创建新用户
            UserProfile.objects.create_user(**form_obj.cleaned_data)
            return redirect('/login/')
        return render(request, 'reg2.html', {'form_obj': form_obj})


@login_required
def customer_list(request):
    current_page = request.GET.get('page', 1)
    query_set = Customer.objects.all()
    total_count = query_set.count()   # SQL语句的效率高
    # 生成一个分页实例
    page_obj = Pagination(current_page,total_count,per_page=2,show_page=2)
    # 取到当前页面的数据
    data = query_set[page_obj.start:page_obj.end]
    # 取到分页的HTML代码
    page_html = page_obj.page_html()
    return render(request, 'customer_list.html', {'customer_list': data, 'page_html': page_html})


def logout(request):
    auth.logout(request)
    return redirect('/login/')


# 添加客户信息
# def add_customer(request):
#     form_obj = CustomerForm()
#     if request.method == 'POST':
#         customer_obj = None
#         form_obj = CustomerForm(request.POST, instance=customer_obj)  # initial最初,初始
#         if form_obj.is_valid():
#             form_obj.save()
#             return redirect('/customer_list/')
#     return render(request, 'add_customer.html', {'form_obj': form_obj})


# 编辑客户信息
# def edit_customer(request, edit_id):
#     print(edit_id)
#     customer_obj = Customer.objects.filter(pk=edit_id).first()
#     # pk是主键的意思,因为id被设置成了主键,所以可以直接写pk=edit_id
#     # 使用instance对象的数据填充生成input标签
#     form_obj = CustomerForm(instance=customer_obj)
#     if request.method == 'POST':
#         # 使用post提交的数据更新到instance中
#         form_obj = CustomerForm(request.POST, instance=customer_obj)
#         if form_obj.is_valid():
#             form_obj.save()
#             return redirect('/customer_list/')
#     return render(request, 'edit_customer.html', {'form_obj': form_obj})


# 把add跟edit放到一个视图函数里
# def customer(request, edit_id=None):
#     # 如果edit_id=None表示是新增操作
#     # 如果edit_id有值表示是编辑操作
#     # ret = Customer.objects.filter(pk=10000000).first()
#     # print(ret)
#     customer_obj = Customer.objects.filter(pk=edit_id).first()  # 如果没有获取到值那么就返回None
#     form_obj = CustomerForm(instance=customer_obj)
#
#     if request.method == 'POST':
#         # 使用POST提交的数据去更新指定的instance实例
#         form_obj = CustomerForm(request.POST, instance=customer_obj)
#         if form_obj.is_valid():
#             print(form_obj)
#             form_obj.save()
#             return redirect('/customer_list/')
#     print(edit_id)
#     return render(request,'customer.html',{'form_obj':form_obj,'edit_id': edit_id})


# 把add和edit放到一个视图函数里面
def customer(request,edit_id=None):
    customer_obj = Customer.objects.filter(pk=edit_id).first()
    form_obj = CustomerForm(instance=customer_obj)
    if request.method == 'POST':
        form_obj = CustomerForm(request.POST,instance=customer_obj)
        if form_obj.is_valid():
            form_obj.save()
            return redirect('/customer_list/')
    return render(request,'customer.html',{'form_obj': form_obj,'edit_id':edit_id})

