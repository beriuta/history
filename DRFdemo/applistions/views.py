from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.views import Response
from rest_framework import serializers
from applistions.serializers import TeacherSerializer, StudentSerializer
from applistions.models import Student, Class, Teacher


# Create your views here.
class TeacherView(APIView):
    def get(self, request):
        teacher_queryset = Teacher.objects.all()
        # 声明一个序列化器
        # 用序列化器去序列化queryset
        ser_obj = TeacherSerializer(teacher_queryset, many=True)  # many=True是序列化的多个
        return Response(ser_obj.data)


class StudentView(APIView):
    def get(self, request):
        student_queryset = Student.objects.all()
        # 声明一个序列化器
        # 用序列化器去序列化queryset
        ser_obj = StudentSerializer(student_queryset, many=True)  # many=True是序列化的多个
        return Response(ser_obj.data)


    # 前端传入的内容{
    #     'id'
    #     'name'
    #     'c_num':{}
    #     'teacher':[]
    #     sex:1
    # }
    def post(self, request):
        # 获取前端的数据
        student_obj = request.data  # 继承APIView没有post方法了,除了get其余的全在data中
        # 用序列化器做校验
        ser_obj = StudentSerializer(data=student_obj)  # 把data拿到StudentSerializer里面做校验
        if ser_obj.is_valid():
            ser_obj.save()
            # 校验的时候要注意与序列化器字段不统一的问题
            print(ser_obj.validated_data)  # 校验通过的数据在这里,但是校验通过之后还是要把新增的内容序列化返回,所以还是在data中
            print('8'* 120)
            return Response(ser_obj.data)  # 校验通过之后的数据也在data里面





