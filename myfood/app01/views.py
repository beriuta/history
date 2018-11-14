from django.shortcuts import render, HttpResponse, redirect, reverse
# from django.urls import reverse


# Create your views here.
# 测试


def c_book(request, year, author):
    # 根据用户查询的url年份不同，返回不用的数据
    print(year, type(year))  # 2018 <class 'str'>
    print(author)
    return render(request, 'book.html')


def blog(request, num=1):
    print(num)
    # return HttpResponse('播了页面')
    return redirect(reverse('xxx'))


def book(request):
    # return HttpResponse('啊啊啊啊啊啊啊啊啊')
    return render(request, 'book_list2.html')


def book_list(request, year, month):
    # return render(request,'book_list2.html')
    return HttpResponse('aaaaaaaaaaaa')