from django.contrib import admin
from crm.models import Customer,Campuses,ClassList
# Register your models here.
# 注册自己写的model类
admin.site.register(Customer)
admin.site.register(ClassList)
admin.site.register(Campuses)