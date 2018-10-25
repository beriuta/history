from django.shortcuts import render
from django.shortcuts import render, HttpResponse,redirect
# Create your views here.
def login(request):
    error_msg = ''
    if request.method == 'POST':
        email = request.POST.get('email', None)
        pwd = request.POST.get('pwd', None)
        if email == 'hanlei@123.com' and pwd == 'hanlei123':
            return redirect('/index/')
    else:
        error_msg = '用户名或密码输入错误！'
    return render(request, 'login.html', {'error_msg': error_msg})


def index(request):
    return render(request, 'index.html')