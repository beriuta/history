from django.shortcuts import render
from django.shortcuts import render,redirect
from appliction.models import UserInfo
# Create your views here.
def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        pwd = request.POST.get('pwd')
        ret = UserInfo.objects.filter(email=email,password=pwd)
        if ret:
            return redirect('https://www.baidu.com')
        else:
            return render(request,'login.html',{'error_msg':'用户名或密码错误！'})
    return render(request,'login.html')
