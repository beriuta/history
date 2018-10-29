from django.db import models


# Create your models here.
# 登录的数据库的用户名或密码
class UserInfo(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
# 导入数据库的时候发生了一个错误  ImportError: cannot import name 'Publisher',是因为我提前在models.py中导入了没有创建好的数据库名称


# 创建出版社表格
class Publisher(models.Model):
    id = models.AutoField(primary_key=True)
    p_name = models.CharField(max_length=30)


# 创建书籍表格
class Book(models.Model):
    id = models.AutoField(primary_key=True)
    b_name = models.CharField(max_length=20)
    publisher = models.ForeignKey(to='Publisher')
