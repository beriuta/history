from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.
class DemoView(APIView):
    def get(self,request,version):
        print(request.version)
        print(request.versioning_scheme)
        if request.version == 'v1':
            return Response('这是第一版本')
        return Response('版本测试借口')