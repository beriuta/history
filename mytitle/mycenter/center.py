"""
这是关于自定义中间件的一些内容
"""

from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse, render, redirect


class M1(MiddlewareMixin):

    def process_request(self, request):
        # 请求进来之后,按照中间件注册顺序执行,返回None则继续执行,返回相应对象,则不继续执行,直接返回响应
        print(request, id(request))
        request.ali = '这可怎么办啊'
        print('这里是自定义中间件M1')

    def process_response(self, request, response):
        # 返回响应之后,按照中间件的倒序执行,必须返回一个相应的对象
        print('这是M1process_resqonse方法')
        return response

    def process_view(self,request,view_func,view_args,view_kwargs):
        # 在request之后,视图函数之前执行,按照中间件注册的顺序执行
        print(view_func)
        print('这是M1的process_view方法')

    def process_template_response(self, request, response):
        # 视图函数中返回带render方法的时候才会触发此方法
        print('这是M1的process_template_response方法')
        return response

    def process_exception(self,request,exception):
        # 当视图函数跑出异常的时候,会触发此方法
        print('这是M1中的process_exception方法')
        print(exception)
        return HttpResponse('视图函数报错了!')




class M2(MiddlewareMixin):
    def process_request(self, request):
        print(request, id(request))
        print('这是自定义中间件M2')

    def process_response(self, request, response):
        print('这是M2process_response的方法')
        return response

    def process_view(self,request,view_func,view_args,view_kwargs):
        # 在request之后,视图函数之前执行,按照中间件注册的顺序执行
        print(view_func)
        print('这是M2的process_view方法')

    def process_template_response(self, request, response):
        print('这是M2的process_template_response方法')
        return response

    def process_exception(self,request,exception):
        # 当视图函数跑出异常的时候,会触发此方法
        print('这是M2中的process_exception方法')
        print(exception)
        return HttpResponse('视图函数报错了!')