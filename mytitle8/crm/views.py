from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from crm.forms2 import RegForm, CustomerForm
from django.contrib import auth
from crm.models import UserProfile, Customer, ConsultRecord
from django import views
from django.utils.decorators import method_decorator
from utils.mypage import Pagination
from django.db.models import Q
from copy import deepcopy


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


class CustomerListView(views.View):  # 增加一个查找功能
    @method_decorator(login_required)
    def get(self, request):
        url_prefix = request.path_info
        print(request.get_full_path())
        print(request.GET)
        qd = deepcopy(request.GET)  # <QueryDict: {'query': ['了']}> 查找的'了',所以query获取的就是登陆者所查找的内容
        qd._mutable = True  # 让QueryDict对象可修改
        print(request.GET.urlencode())  # 把检索参数都编码成URL
        current_page = request.GET.get('page', 1)
        if '/my_customer/' in request.path_info:
            # 获取私户信息,Customer类中查找consultant这个字段属于是当前销售用户的客户
            query_set = Customer.objects.filter(consultant=request.user)  # 获取此时登录的销售用户的名称
        else:
            # 获取公户的所有信息
            query_set = Customer.objects.filter(consultant__isnull=True)  # 把consultant这个字段为空的都提取出来
        # 根据模糊检索的条件对query_set再做过滤
        # 找到name,qq,qq_name字段包含QuerySet_value的那些数据就是搜索的结果
        q = self._get_query_q(['name', 'qq', 'qq_name'])
        query_set = query_set.filter(q)
        # query_set = Customer.objects.all()
        # total_count = query_set.count()   # SQL语句的效率高
        # 生成一个分页实例
        page_obj = Pagination(current_page, query_set.count(), url_prefix, per_page=2)
        print(page_obj.start, page_obj.end)
        # 取到当前页面的数据
        data = query_set[page_obj.start:page_obj.end]
        # 取到分页的HTML代码
        page_html = page_obj.page_html()
        return render(request, 'customer_list.html', {'customer_list': data, 'page_html': page_html})

    @method_decorator(login_required)
    def post(self, request):
        """批量操作,变公户/私户"""
        print(request.POST)
        cid = request.POST.getlist('cid')  # 获取要操作的客户的id,因为是可以批量获取,所以不止一个,使用getlist
        action = request.POST.get('action')
        # 判断self 是否有一个_action的方法,如果有就执行,否则就返回个"滚"
        if not hasattr(self, '_{}'.format(action)):
            return HttpResponse('滚')
        getattr(self, '_{}'.format(action))(cid)
        return redirect('/customer_list/')
        # if action == 'to_private':  # 批量添加时
        #     # 方法1: 找到所有要操作得到客户数据,把他们变成我的客户
        #     # 把获取的id值查找出来,统一在consultant字段中添加上登录销售的名字
        #     Customer.objects.filter(id__in=cid).update(consultant=request.user)
        #     # 方法2: 把要操作的客户添加到我的客户列表中
        #     # request.user是一个对象,customers是反向查找的那个名字,如果没有那个名字,就用 表名_set
        #     request.user.customers.add(*Customer.objects.filter(id__in=cid))  # 一定记得打散,因为查找的id不一定是只有一个
        # elif action == 'to_public':  # 批量删除时
        #     # 方法1:找到所有要操作的客户数据,把他们的销售字段设置为空
        #     Customer.objects.filter(id__in=cid).update(consultant=None)
        #     # 方法2:从我的客户列表里面把指定的客户删除
        #     # request.user.customers.remove(*Customer.objects.filter(id__in=cid))
        # return redirect('/customer_list/')

    def _to_private(self, cid):  # 私户
        # 方法1:找到所有要操作的客户数据,把他们的销售字段设置为空
        Customer.objects.filter(id__in=cid).update(consultant=None)
        # 方法2:把要操作的客户添加到我的客户列表里
        self.request.user.customers.add(*Customer.objects.filter(id__in=cid))

    def _to_public(self, cid):
        # 方法1:找到所有操作的客户数据,把他们的销售字段设置为空
        Customer.objects.filter(id__in=cid).update(consulatant=None)
        # 方法2:从我的客户列表里面把指定的客户删除
        self.request.user.customers.remov(*Customer.objects.filter(id__in=cid))

    def _get_query_q(self, field_list, op='OR'):
        # 从URL中取到query参数
        query_value = self.request.GET.get('query', '')
        q = Q()
        # 指定Q查询内部的操作是OR还是AND
        q.connector = op
        # 遍历要检所的字段,挨个添加子Q对象
        for field in field_list:  # Q(name__icontains='帅')  field_list=[['name','qq','qq_name']]
            q.children.append(Q(('{}__icontains'.format(field), query_value)))
        return q


# @login_required
# # 我的客户列表-->私户或者公户 --->get请求函数版本
# def customer_list(request):
#     url_prefix = request.path_info
#     print(request.get_full_path())
#     current_page = request.GET.get('page', 1)
#     if '/my_customer/' in request.path_info:
#         # 获取私户信息,Customer类中查找consultant这个字段属于是当前销售用户的客户
#         query_set = Customer.objects.filter(consultant=request.user)  # 获取此时登录的销售用户的名称
#     else:
#         # 获取公户的所有信息
#         query_set = Customer.objects.filter(consultant__isnull=True)  # 把consultant这个字段为空的都提取出来
#
#     # query_set = Customer.objects.all()
#     # total_count = query_set.count()   # SQL语句的效率高
#     # 生成一个分页实例
#     page_obj = Pagination(current_page, query_set.count(), url_prefix, per_page=2)
#     # 取到当前页面的数据
#     data = query_set[page_obj.start:page_obj.end]
#     # 取到分页的HTML代码
#     page_html = page_obj.page_html()
#     return render(request, 'customer_list.html', {'customer_list': data, 'page_html': page_html})


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
@login_required
def customer(request, edit_id=None):
    customer_obj = Customer.objects.filter(pk=edit_id).first()
    form_obj = CustomerForm(instance=customer_obj)
    if request.method == 'POST':
        form_obj = CustomerForm(request.POST, instance=customer_obj)
        if form_obj.is_valid():
            form_obj.save()
            return redirect('/customer_list/')
    return render(request, 'customer.html', {'form_obj': form_obj, 'edit_id': edit_id})


# 展示沟通记录
@login_required
def consult_record_list(request):
    query_set = ConsultRecord.objects.filter(consultant=request.user, delete_status=False)
    return render(request, 'consult_record_list.html', {'consult_record': query_set})


# 新增和编辑放在一个视图函数里
@login_required
def consult_record(request, edit_id=None):
    record_obj = ConsultRecord.objects.filter(id=edit_id).first()  # None
    if not record_obj:
        record_obj = ConsultRecord(consultant=request.user)  # 生成一个销售是登录者的ConsultRecord对象
        print(record_obj, id(record_obj))
        print('@' * 120)
    form_obj = ConsultRecord(instance=record_obj, initial={'consultant': request.user})  # initial初始化,默认值
    return render(request, 'consult_record.html', {'form_obj': form_obj, 'edit_id': edit_id})
