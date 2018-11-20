from django.shortcuts import render
from applications.forms import RegForm
from applications.models import UserInfo
from django.http import JsonResponse

# Create your views here.


def reg(request):
    if request.method == 'POST':
        res = {'code':0}
        form_obj2 = RegForm(request.POST)
        if form_obj2.is_valid():
            form_obj2.cleaned_data.pop('re_password')
            UserInfo.objects.create(**form_obj2.cleaned_data)
            res['url'] = '/login/'
        else:
            res['code'] = 1
            res['error_msg'] = form_obj2.errors

        return JsonResponse(res)

    form_obj = RegForm()
    return render(request,'reg.html',{'form':form_obj})