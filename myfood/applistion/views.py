from django.shortcuts import render, redirect, HttpResponse
from applistion.models import UserInfo, Publisher, Book, Author


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


# 查看出版社，单表查询
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
    if request.method == 'POST':
        new_name = request.POST.get('name')
        print(new_name)
        new_id = request.POST.get('id')
        data = Publisher.objects.get(id=new_id)  # 这边一个错误，get写成了create，create是更新
        data.p_name = new_name
        data.save()
        return redirect('/publisher_list/')
    a = request.GET.get('id')
    data = Publisher.objects.get(id=a)
    return render(request, 'edit_publisher.html', {'obj': data})


# 查看书籍和出版社，联表查询
def book_list(request):
    book_all = Book.objects.all()
    publisher_all = Publisher.objects.all()
    return render(request, 'book_list.html', {'book_list': book_all, 'publisher_list': publisher_all})


# 删除书籍
def delete_book(request):
    delete_id = request.GET.get('id')
    Book.objects.get(id=delete_id).delete()
    return redirect('/book_list/')


# 增加书籍
def add_book(request):
    if request.method == 'POST':
        b_name = request.POST.get('book')
        p_id = request.POST.get('id')
        Book.objects.create(b_name=b_name, publisher_id=p_id)
        return redirect('/book_list/')
    publisher_all = Publisher.objects.all()
    return render(request, 'add_book.html', {'publisher_list': publisher_all})


# 修改书籍
def edit_book(request):
    b_id = request.GET.get('id')
    print(b_id)
    book_obj = Book.objects.get(id=b_id)
    if request.method == 'POST':
        b_name = request.POST.get('book')
        p_id = request.POST.get('p_id')
        book_obj.b_name = b_name
        book_obj.publisher_id = p_id
        book_obj.save()
        return redirect('/book_list/')
    all_p = Publisher.objects.all()
    return render(request, 'edit_book.html', {'book': book_obj, 'publisher_list': all_p})


# 查看作者跟书籍，多表查询
def author_list(request):
    pass


# 删除作者跟书籍
def delete_author(request):
    pass


# 添加作者跟书籍
def add_author(request):
    pass


# 修改作者跟书籍
def edit_author(request):
    pass
