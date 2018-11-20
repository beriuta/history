"""
此文件写有自定义登录验证的中间件
自定义访问频率限制的中间件
"""
from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import render, HttpResponse, redirect
from applistions.models import UserInfo
from django.conf import settings
import time


class CheckLogin(MiddlewareMixin):

    def process_request(self, request):
        # 判断当前访问的URL是不是在白名单中
        white_url = settings.WHITE_URLS if hasattr(settings, 'WHITE_URLS') else []
        # 如果settings文件里面有WHITE_URL就返回if前面的,如果没有就返回else后面的空列表
        if request.path_info in white_url:
            return None
        user_id = request.session.get('user', None)
        if not user_id:
            return redirect('/login/')
        else:
            user_obj = UserInfo.objects.get(id=user_id)
            request.user = user_obj


ACCESS_RECORD = {}


# 自定义访问频率限制的中间件
class Throttle(MiddlewareMixin):

    def process_request(self, request):
        access_limit = settings.ACCESS_LIMIT if hasattr(settings, 'ACCESS_LIMIT') else 60
        # 当前请求的IP地址
        ip = request.META.get('REMOTE_ADDR')
        if ip not in ACCESS_RECORD:
            ACCESS_RECORD[ip] = []

        history = ACCESS_RECORD[ip]
        # 判断最近的10秒钟之内这个IP访问次数是否大于3
        now = time.time()
        # DRF 访问频率限制
        while history and now - history[-1] > access_limit:
            history.pop()
        history.insert(0, now)
        if len(history) > 3:
            return HttpResponse('滚')
