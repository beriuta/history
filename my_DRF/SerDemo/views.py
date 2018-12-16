from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from SerDemo.models import Book, Publisher, Author
from django.views import View
from rest_framework.response import Response
from SerDemo.serializers import BookSerializer
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSetMixin
from django.core import serializers
import json


# Create your views here.
# # 用values实现序列化
# class BookView(View):
#     # def get(self, request):
#     #     book_queryset = Book.objects.values('id', 'title', 'category', 'pub_time', 'publisher')
#     #     # # queryset = [{},{}]
#     #     book_list = list(book_queryset)
#     #      # ret = json.dumps(book_list,ensure_ascii=False)  # ensure_ascii=False不生成ASX码
#     #      # return HttpResponse(ret)  # 一般不用json,太麻烦,并且不能序列化datetime类型的数据,有现有的模块JsonResponse
#     #     ret = []
#     #     for book in book_list:
#     #         print(book)
#     #         # 因为publisher是外键关联,获取的是id值,所以根据id值跨表查询获取到具体的字段信息,赋值给book中的publisher这个键
#     #         publisher_obj = Publisher.objects.filter(id=book['publisher']).first()
#     #         book['publisher'] = [
#     #             {
#     #                 'id': publisher_obj.id,
#     #                 'title': publisher_obj.title,
#     #             }
#     #         ]
#     #         ret.append(book)
#     #     return JsonResponse(ret, safe=True, json_dumps_params={"ensure_ascii": False})
#     # 第二版
#     def get(self,request):
#         book_queryset = Book.objects.all()
#         ret = serializers.serialize('json',book_queryset,ensure_ascii=False)
#  第一个参数是什么格式的,第二个参数是要转化的数据,第三个参数是默认ASX编码,设置成False,就不是默认的

# # 用序列化器实现序列化
# class BookView(APIView):
#     def get(self, request):
#         # 获取所有的Book表中的数据
#         book_queryset = Book.objects.all()
#         # 声明一个序列化器,用序列化器去序列化QuerySet
#         set_obj = BookSerializer(book_queryset, many=True)
#         return Response(set_obj.data)
#
#     def post(self, request):
#         # 获取前端传来的数据
#         book_obj = request.data
#         # 用序列化器做校验
#         ser_obj = BookSerializer(data=book_obj)
#         # 更新
#         if ser_obj.is_valid():
#             ser_obj.save()
#             return Response(ser_obj.data)  # 更新成功
#         return Response(ser_obj.errors)  # 错误信息
#
#
# class BookEditView(APIView):
#     def get(self, request, id):
#         book_obj = Book.objects.filter(id=id).first()
#         ser_obj = BookSerializer(book_obj)
#         return Response(ser_obj.data)
#
#     def put(self, request, id):
#         book_obj = Book.objects.filter(id=id).first()
#         ser_obj = BookSerializer(instance=book_obj, data=request.data, partial=True)
#         # 一般来说，partial用于检查客户端向视图提交数据时是否需要模型中的字段进行字段验证
#         if ser_obj.is_valid():
#             ser_obj.save()
#             return Response(ser_obj.data)  # 更新成功
#         return Response(ser_obj.errors)
#
#     def delete(self, request, id):
#         book_obj = Book.objects.filter(id=id).first()
#         if book_obj:
#             book_obj.delete()
#             return Response('')
#         return Response('删除的对象不存在')

# -------------------以上是用了两个类来封装,但是如果是多张表逻辑不变,只需要更改序列化器-------------------
# -------------------以下是将五个方法提取出来封装成类,用于继承-------------------


# # 封装视图,将上面的五个方法提取出来,封装成类
# class GenericAPIView(APIView):  # 封装了一个通用的类
#     query_set = None  # 每个类都有queryset方法,但是都不一样,所以定义为None,如果有自己的值就覆盖
#     serializer_class = None  # 每个类都有序列化器
#
#     def get_queryset(self):
#         return self.query_set  # 定义一个方法,返回的是query_set静态方法
#
#     def get_serializer(self, *args, **kwargs):
#         return self.serializer_class(*args, **kwargs)  # 返回的是序列化器接受的queryst,跟many=True
#
#
# class ListModelMixin(object):  # 把get方法封装成了一个类
#     def list(self, request):
#         queryset = self.get_queryset()
#         ser_obj = self.get_serializer(queryset, many=True)
#         print(ser_obj)  # 返回的是一个序列化对象
#         return Response(ser_obj.data)  # Response里面含有json,是把校验通过的数据序列化到前端
#
#
# class CreateModelMixin(object):  # 更新数据,post请求
#     def create(self, request):
#         # 获取前端传过来的数据
#         obj = request.data
#         # 用序列化器做校验
#         ser_obj = self.get_serializer(data=obj)
#         if ser_obj.is_valid():
#             ser_obj.save()
#             print(ser_obj.validated_data)
#             return Response(ser_obj.data)
#         return Response(ser_obj.errors)
#
#
# class RetrieveModelMixin(object):  # get请求,查看某个id的数据
#     def retrieve(self, request, id):
#         book_obj = self.get_queryset().filter(id=id).first()
#         ser_obj = self.get_serializer(book_obj)
#         return Response(ser_obj.data)
#
#
# class UpdateModelMixin(object):  # put请求,根据id获取要修改的字段
#     def update(self, request, id):
#         book_obj = self.get_queryset().filter(id=id).first()
#         ser_obj = self.get_serializer(instance=book_obj, data=request, partial=True)
#         if ser_obj.is_valid():
#             ser_obj.save()
#             return Response(ser_obj.data)
#         return Response(ser_obj.errors)
#
#
# class DestroyModelMixin(object):
#     def destroy(self, request, id):
#         book_obj = self.get_queryset().filter(id=id).first()
#         if book_obj:
#             book_obj.delete()
#             return Response('')
#         return Response('删除的对象不存在')
#
#
# # 将类都继承
# class ListCreateModelMixin(GenericAPIView, ListModelMixin, CreateModelMixin):
#     pass
#
#
# class RetrieveUpdateDestroyModelMixin(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
#     pass
#
#
# class ModelViewSet(ViewSetMixin, ListCreateModelMixin, RetrieveUpdateDestroyModelMixin):
#     pass
#
#
# # 重写 BookEditView 这个类
# class BookEditView(RetrieveUpdateDestroyModelMixin):
#     query_set = Book.objects.all()
#     serializer_class = BookSerializer
#
#     def get(self, request, id):
#         return self.retrieve(request, id)  # RetrieveModelMixin里面的retrieve方法
#
#     def put(self, request, id):
#         return self.update(request, id)
#
#     def delete(self, request, id):
#         return self.destroy(request, id)


# ---------------------把两个类合并成一个类,按照两个路由返回的的参数返回方法,第三次封装-------------
# 这是自己写的
# class BookModelView(ModelViewSet):
#     query_set = Book.objects.all()
#     serializer_class = BookSerializer
# 用一个视图函数来解决两个路由的分配
from rest_framework.viewsets import ModelViewSet


# 这是rest_framework框架自带的模块,这里的参数是queryset,而自己写的则是query_set
class BookModelView(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


##############################################################3
# 上面自己写的继承类的五个方法,在rest_framework中已经有了
from django.test import TestCase
from rest_framework import views
from rest_framework import viewsets
from rest_framework import mixins
from rest_framework import generics
