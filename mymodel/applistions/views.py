from django.shortcuts import render,HttpResponse
from applistions.models import UserInfo,Blog

# Create your views here.
def home(request):
    # 查找第一个用户
    user_obj = UserInfo.objects.all()[0]
    print(user_obj.name,type(user_obj.name))
    print(user_obj.birthday,type(user_obj.birthday))
    print(user_obj.gender,type(user_obj.gender))
    print(user_obj.get_gender_display())  # 专门用来获取choice字段的显示值

def blog(request):
    blog_obj = Blog.objects.all()[0]
    blog_obj.title = 'Django一点都不难！'
    blog_obj.save()
    return HttpResponse('ok')