from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, REDIRECT_FIELD_NAME
from django.shortcuts import render, redirect
from applstions.models import Student, Class, Teacher
from applstions.forms import RegForm

from django.contrib import auth


# Create your views here.
# 登录
def login(request):
    if request.method == 'POST':
        user = request.POST.get('user')
        pwd = request.POST.get('pwd')
        remember = request.POST.get('remember')
        user_obj = auth.authenticate(username=user,password=pwd)
        if user_obj:
            # 设置session
            auth.login(request, user_obj)
            next_url = request.GET.get(REDIRECT_FIELD_NAME, '/class_list/')
            if remember:
                request.session.set_expiry(7*24*60*60)
            else:
                request.session.set_expiry(0)
            return redirect(next_url)
        else:
            return render(request, 'login.html', {'error_msg': '用户名或密码错误'})
    return render(request, 'login.html')


# 注册
def rag(request):
    if request.method == 'POST':
        form_obj = RegForm(request.POST)
        if form_obj.is_valid():
            username = request.POST.get('username')
            pwd = request.POST.get('password')
            User.objects.create_user(username=username,password=pwd)
            return redirect('/login/')
        else:
            return render(request,'rag.html',{'form': form_obj})
    form_obj = RegForm()
    return render(request, 'rag.html',{'form':form_obj})


# 注销
@login_required
def logout(request):
    auth.logout(request)
    return redirect('/login/')


# 修改密码
@login_required
def change_pwd(request):
    if request.method == 'POST':
        old_pwd = request.POST.get('password')
        is_ok = request.user.check_password(old_pwd)
        if is_ok:
            new_pwd = request.POST.get('new_password')
            request.user.set_password(new_pwd)
            request.user.save()
            return redirect('/login/')
    return render(request, 'change_pwd.html')

# 登陆之后查看学生管理系统


# 查看班级
@login_required
def class_list(request):
    ret = Class.objects.all()
    return render(request, 'class_list.html', {'class_list': ret})


# 删除班级
@login_required
def delete_class(request):
    delete_id = request.GET.get('id')
    Class.objects.get(id=delete_id).delete()
    return redirect('/class_list/')


# 增加班级
@login_required
def add_class(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        Class.objects.create(c_name=name)
        return redirect('/class_list/')
    return render(request, 'add_class.html')


# 编辑班级
@login_required
def edit_class(request):
    c_id = request.GET.get('id')
    ret = Class.objects.get(id=c_id)
    if request.method == 'POST':
        new_name = request.POST.get('name')
        ret.c_name = new_name
        ret.save()
        return redirect('/class_list/')
    return render(request, 'edit_class.html', {'class': ret})


# 查看学生
@login_required
def student_list(request):
    ret = Student.objects.all()
    return render(request, 'student_list.html', {'student_list': ret})


# 删除学生
@login_required
def delete_student(request):
    s_id = request.GET.get('id')
    Student.objects.get(id=s_id).delete()
    return redirect('/student_list/')


# 增加学生
@login_required
def add_student(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        class_id = request.POST.get('id')
        print(class_id)
        Student.objects.create(s_name=name, class_name_id=class_id)
        return redirect('/student_list/')
    class_obj = Class.objects.all()
    return render(request, 'add_student.html', {'class_list': class_obj})


# 编辑学生
@login_required
def edit_student(request):
    ret = request.GET.get('id')
    s_obj = Student.objects.get(id=ret)
    if request.method == 'POST':
        s_name = request.POST.get('name')
        c_id = request.POST.get('id')
        s_obj.s_name = s_name
        s_obj.class_name_id = c_id
        s_obj.save()
        return redirect('/student_list/')
    c_name = Class.objects.all()
    return render(request, 'edit_student.html', {'student': s_obj, 'class_list': c_name})


# 查看老师
@login_required
def teacher_list(request):
    ret = Teacher.objects.all()
    return render(request, 'teacher_list.html', {'teacher_list': ret})


# 删除老师
@login_required
def delete_teacher(request):
    ret = request.GET.get('id')
    Teacher.objects.get(id=ret).delete()
    return redirect('/teacher_list/')


# 增加老师
@login_required
def add_teacher(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        c_id = request.POST.getlist('id')  # 一个老师可以带多个班级PRIMARY
        t_obj = Teacher.objects.create(t_name=name)
        t_obj.save()
        t_obj.class_name.add(*c_id)
        return redirect('/teacher_list/')
    obj = Class.objects.all()
    return render(request, 'add_teacher.html', {'class_list': obj})


# 编辑老师
@login_required
def edit_teacher(request):
    ret = request.GET.get('id')
    obj = Teacher.objects.get(id=ret)
    if request.method == 'POST':
        name = request.POST.get('name')
        c_id = request.POST.get('id')
        t_obj = Teacher.objects.get(id=ret)
        t_obj.t_name = name
        t_obj.save()
        t_obj.class_name.set(c_id)
        return redirect('/teacher_list/')
    class_list1 = Class.objects.all()
    return render(request, 'edit_teacher.html', {'teacher': obj, 'class_list': class_list1})


def t(request):
    return render(request, 't.html')