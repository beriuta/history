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


# # 增加书名跟出版社名,无模态框
# def add_book(request):
#     if request.method == 'POST':
#         book_name = request.POST.get('b_name')
#         publisher_id = request.POST.get('id')
#         data = Book.objects.create(b_name=book_name, publisher_id=publisher_id)
#         return redirect('/select_book/')
#     return render(request, 'add_book.html')


# 增加书名跟出版社名,点击出现模态框
def add_book(request):
    b_name = request.POST.get('b_name')
    publisher_id = request.POST.get('publisher')
    # Book.objects.create(b_name=b_name, publisher_id=publisher_id)
    Book.objects.create(b_name=b_name, publisher=Publisher.objects.get(id=publisher_id))
    return request('/select_book/')  # 循环出版社名称时一直显示不出来


# 删除书名和出版社，结果全部删除了
def delete_book(request):
    delete_id = request.GET.get('id')
    Book.objects.filter(id=delete_id).delete()  # 这边用了get
    return redirect('/select_book/')


# 修改书名跟出版社名
def edit_book(request):
    # 先获取要编辑的书籍的id
    b_id = request.GET.get('id')
    # 在获取要编辑的书籍的对象
    b_obj = Book.objects.get(id=b_id)
    # 判断是否是POST
    if request.method == 'POST':
        new_b_name = request.POST.get('b_name')
        new_p_id = request.POST.get('publisher')
        b_obj.b_name = new_b_name
        b_obj.publisher_id = new_p_id
        b_obj.save()
        return redirect('/select_book/')  # 这个跳转不成功
    # 拿到所有的出版社数据，用来展示页面上的select标签
    all_publisher = Publisher.objects.all()
    return render(request,'edit_book.html',{'book':b_obj,'publisher_list':all_publisher})


# 查看书籍名跟出版社名
def select_book(request):
    all_book = Book.objects.all()
    all_publisher = Publisher.objects.all()
    return render(request, 'select_book.html', {'book_list': all_book, 'publisher': all_publisher})
