from django.shortcuts import render, redirect
from applition.models import UserInfo, Publisher


# Create your views here.
# 登录功能
def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        pwd = request.POST.get('pwd')
        ret = UserInfo.objects.filter(email=email, password=pwd)
        if ret:
            return redirect('https://www.baidu.com/')
        else:
            return render(request, 'login.html', {'error_msg': '用户名或密码输入错误！'})
    return render(request, 'login.html')


# 出版社列表页面的处理函数
def publisher_list(request):
    ret = Publisher.objects.all()  # 获取全部的
    return render(request, 'publisher_list.html', {'publisher_list': ret})


# 增加内容到表格里
def add_publisher(request):
    if request.method == 'POST':
        new_name = request.POST.get('name')
        Publisher.objects.create(name=new_name)
        return redirect('/publisher_list/')
    return render(request, 'add_publisher.html')


# 修改表格里的内容
def edit_publisher(request):
    if request.method == 'POST':
        edit_id = request.POST.get('id')
        edit_name = request.POST.get('name')
        edit_obj = Publisher.objects.get(id=edit_id)
        edit_obj.name = edit_name
        edit_obj.save()  # 手动将改动提交到数据库内
        return redirect('/publisher_list/')
    # 用户第一次跳转是GET请求，需要给用户的信息有：
    # 1. 获取要编辑的出版社的id
    edit_id = request.GET.get('id')
    # 2.根据id去数据库拿到要编辑就的出版社数据
    ret = Publisher.objects.get(id=edit_id)
    print(ret, type(ret))
    # 3.在页面上显示要编辑的出版社的信息
    return render(request, 'edit_publisher.html', {'obj': ret})  # 把ret传入HTML页面，字符串替换


# 删除表格里的内容
def delete_publisher(request):
    # 获取用户要删除的id
    delete_id = request.GET.get('id')
    # 根据id到数据库删除数据
    ret = Publisher.objects.get(id=delete_id).delete()
    # 给用户返回删除成功的画面
    return redirect('/publisher_list/')
