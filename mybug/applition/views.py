from django.shortcuts import render, redirect, HttpResponse
from applition.models import Info, Pulisher, Book


# Create your views here.
# 登录系统
def login(request):
    # 判断是否是post
    if request.method == 'POST':
        # 如果是，获取用户输入的内容
        user = request.POST.get('user')  # 这边犯了一个错，写成了Info.objects.get
        pwd = request.POST.get('pwd')
        # 根据用户输入的内容跟数据库的内容作对比
        ret = Info.objects.filter(username=user, password=pwd)
        # 如果正确，就return一个百度页面
        if ret:
            return redirect('/select_publisher/')
        # 如果不正确，还是return一个login页面，不过下面加上一句提示登录失败的话
        else:
            return render(request, 'login.html', {'error_msg': '用户名或密码输入错误！'})
    # 不是就return一个loginHTML页面
    return render(request, 'login.html')


# 查看表格出版社内容
def select_publisher(request):
    # 获取数据库里的内容
    sph = Pulisher.objects.all()
    # 返回一个HTML页面
    return render(request, 'select_publisher.html',
                  {'select_publisher': sph})  # 因为select_publisher.html里面的p_name写成了name


# 增加出版社的名字
def add_publisher(request):
    # 判断是否是POST
    if request.method == 'POST':
        # 是，获取用户输入的内容
        add_name = request.POST.get('name')
        print(add_name)
        # 连接数据库，将内容添加到里面
        Pulisher.objects.create(p_name=add_name)  # 这里出了一个问题，数据库添加参数的时候一定要写上添加的是哪个，这里没写p_name报错了
        # 给用户返回一个成功添加进去的表格页面
        return redirect('/select_pulisher/')  # 这里出了一个问题，输入添加的内容没有成功跳转页面，是因为add_pulisher.html里面的按钮不是submit
    # 不是，返回一个add的HTML页面里面
    return render(request, 'add_publisher.html')  # 这里出了一个错误，是返回的一个HTML文件，不是一个‘/add_publisher/’


# 删除出版社的名字
def delete_publisher(request):
    # 点击删除按钮，跳转到delete页面，根据id到数据库删除相应的内容
    ret = request.GET.get('id')
    Pulisher.objects.get(id=ret).delete()
    # 返回一个删除后的HTML页面
    return redirect('/select_publisher/')


# 修改出版社名字
def alter_publisher(request):
    # 判断是否是POST
    if request.method == 'POST':
        # 如果是，获取这个input框里的内容
        ret_id = request.POST.get('id')
        ret_name = request.POST.get('name')
        # 根据id提取数据库的内容，直接对内容进行修改
        obj = Pulisher.objects.get(id=ret_id)
        # 更新一下数据库的内容，因为此次操作是单单在Python层面上的
        obj.p_name = ret_name
        obj.save()  # 错误，跳转到页面但是没有修改完成，忘记加save()
        return redirect('/select_publisher/')
    # 不是，到数据库获取这个id的内容
    ret_id = request.GET.get('id')
    # 到数据库里面按照id查找内容
    ret = Pulisher.objects.get(id=ret_id)
    # print(ret,type(ret))  #  是一个Publisher对象
    # 跳转页面，在input框里放入已有的内容
    return render(request, 'alter_publisher.html',
                  {'obj': ret})  # 错误，跳转到alter_publisher页面了但是input框里没有数据库内的内容,因为alter_publisher里面的obj.p_name写成了obj.name
    # return HttpResponse('要编辑了')  # 一直卡了很久是因为这边获取的是‘id’，而select里面的编辑按钮上面的?id={{ publisher.name }}是获取的name


def book_list(request):
    data = Book.objects.all()
    return render(request, 'book_list.html', {'book_list': data})

def delete_book(request):
    ret = request.GET.get('id')
    Book.objects.filter(id=ret).delete()
    return redirect('/book_list/')
