from django.shortcuts import render, redirect, HttpResponse
from applisitons.models import Auther, Publisher, Book
from django.views import View
import json


# Create your views here.
class PublisherView(View):
    def get(self, request):
        publisher_obj = Publisher.objects.all()
        ret = []
        for publisher in publisher_obj:
            print(publisher.id)
            dict = {
                'id': publisher.id,
                'name': publisher.name
            }
            ret.append(dict)
        ret2 = json.dumps(ret, ensure_ascii=False)
        return HttpResponse(ret2)

    def post(self, request):
        return HttpResponse('ok')


class AutherView(View):
    def get(self, request):
        auther_obj = Auther.objects.all()
        ret = []
        for auther in auther_obj:
            print(auther_obj.id)
            dict = {
                'id': auther.id,
                'age': auther.age,
                # 'books': auther.books
            }
            ret.append(dict)
        ret2 = json.dumps(ret, ensure_ascii=False)
        return HttpResponse(ret2)
