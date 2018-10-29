from django.shortcuts import render, redirect
from applstion.models import UserInfo, Publisher, Book


# Create your views here.
# 登录功能
def login(request):
    if request.method == 'POST':
        user = request.POST.get('user')
        pwd = request.POST.get('pwd')
        if UserInfo.objects.filter(username=user, password=pwd):
            return redirect('/publisher_list/')
        return render(request, 'login.html', {'error_msg': '用户名或密码输入错误！'})
    return render(request, 'login.html')


# 查看出版社名称
def publisher_list(request):
    # 获取数据库出版社所有的内容
    data = Publisher.objects.all()
    return render(request, 'publisher_list.html', {'publisher_list': data})


# 增加出版社名称
def add_publisher(request):
    if request.method == 'POST':
        p_name = request.POST.get('name')
        Publisher.objects.create(p_name=p_name)
        return redirect('/publisher_list/')
    return render(request, 'add_publisher.html')


# 删除出版社名称
def delete_publisher(request):
    delete = request.GET.get('id')  # id 一定是"/delete_publisher/?id={{ publisher.id }}"的id
    Publisher.objects.get(id=delete).delete()
    return redirect('/publisher_list/')


# 修改出版社名称
def edit_publisher(request):
    # 判断是否是post
    if request.method == 'POST':
        # 如果是，获取用户输入的内容
        new_name = request.POST.get('name')
        new_id = request.POST.get('id')
        data = Publisher.objects.get(id=new_id)
        data.p_name = new_name
        data.save()  # 更新到数据库中
        return redirect('/publisher_list/')
    # 获取数据库里的内容
    data_id = request.GET.get('id')
    data = Publisher.objects.get(id=data_id)  # 总是忘记前面写id=或者name=一定记得要写对应关系，不然数据库不知道怎么对应找
    # 不是 ，点击编辑按钮，获取编辑页面
    return render(request, 'edit_publisher.html', {'obj': data})


# 增加书名跟出版社名
def add_book(request):
    pass


# 删除书名
def delete_book(request):
    pass


# 修改书名跟出版社名
def edit_book(request):
    pass


# 查看书籍名跟出版社名
def select_book(request):
    pass
