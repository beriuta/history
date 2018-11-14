from django.shortcuts import render, redirect, HttpResponse
from applistions.models import UserInfo
from functools import wraps


# Create your views here.


def coklin_login(func):
    @wraps(func)
    def inner(request, *args, **kwargs):
        session_user = request.session.get('name', None)
        if session_user:
            rep = func(request, *args, **kwargs)
            return rep
        else:
            return_url = request.path_info
            print(return_url)
            return redirect('/login/?Nexurl={}'.format(return_url))
    return inner


@coklin_login
def login(request):
    if request.method == 'POST':
        user = request.POST.get('user')
        pwd = request.POST.get('pwd')
        ret_obj = UserInfo.objects.filter(username=user, password=pwd).first()
        print(UserInfo.objects.filter(username=user, password=pwd))
        if ret_obj:
            request_url = request.GET.get('Nexurl', '/home/')
            print(request_url)
            request.session['name'] = ret_obj.username
            request['age'] = 12
            request['hobby'] = '吃'
            return redirect(request_url)

    return render(request, 'login.html')


@coklin_login
def home(request):
    return HttpResponse('这是home页面')
