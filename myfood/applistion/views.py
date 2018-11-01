from django.shortcuts import render, redirect, HttpResponse
from applistion.models import UserInfo, Publisher


# Create your views here.
# 登录功能
def login(request):
    if request.method == 'POST':
        user = request.POST.get('name')
        pwd = request.POST.get('pwd')
        if UserInfo.objects.filter(name=user, password=pwd):
            return redirect('/publisher_list/')
            # return HttpResponse('要登录了')
        else:
            return render(request, 'login.html', {'error_msg': '用户名或密码错误！'})
    return render(request, 'login.html')


# 查看出版社
def publisher_list(request):
    data = Publisher.objects.all()
    return render(request, 'publisher_list.html', {'publisher_list': data})


# 增加出版社
def add_publisher(request):
    if request.method == 'POST':
        name = request.POST.get('p_name')
        Publisher.objects.create(p_name=name)
        return redirect('/publisher_list/')
    return render(request, 'add_publisher.html')


# 删除出版社
def delete_publisher(request):
    delete_id = request.GET.get('id')
    Publisher.objects.get(id=delete_id).delete()
    return redirect('/publisher_list/')


# 编辑修改出版社
def edit_publisher(request):
    pass
