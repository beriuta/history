from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from AuthDemo.models import UserInfo
from utils.auth import Myauth
from utils.permission import MyPermission
import uuid


# Create your views here.
class AuthView(APIView):
    def get(self, request):
        return Response('认证组件接口')

    def post(self, request):
        name = request.data.get('name', '')
        pwd = request.data.get('pwd', '')
        if name and pwd:
            # 创建用户
            UserInfo.objects.create(username=name, password=pwd)
            return Response('注册成功')
        return Response('注册失败')


class LoginView(APIView):
    def post(self, request):
        name = request.data.get('name', '')
        pwd = request.data.get('pwd', '')
        user_obj = UserInfo.objects.filter(username=name, password=pwd).first()
        if user_obj:
            token = uuid.uuid4()
            user_obj.token = token
            user_obj.save()
            return Response('登陆成功')
        return Response('登录失败')


# 测试认证
class TestView(APIView):
    authentication_classes = [Myauth, ]

    def get(self, request):
        print(request.user)
        print(request.auth)
        return Response('登陆之后发送的数据')


# 测试权限
class PermissionView(APIView):
    authentication_classes = [Myauth, ]  # 认证之后才会有权限
    permission_classes = [MyPermission, ]

    def get(self,request):
        # 这个接口只能vip用户访问
        return Response('权限测试借口')









