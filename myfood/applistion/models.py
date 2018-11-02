from django.db import models


# Create your models here.
# 登录用户名和密码表格
class UserInfo(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    password = models.CharField(max_length=20)


# 出版社表格
class Publisher(models.Model):
    id = models.AutoField(primary_key=True)
    p_name = models.CharField(max_length=20)


# 书籍表格
class Book(models.Model):
    id = models.AutoField(primary_key=True)
    b_name = models.CharField(max_length=20)
    publisher = models.ForeignKey(to='Publisher')


# 作者表格
class Author(models.Model):
    id = models.AutoField(primary_key=True)
    a_name = models.CharField(max_length=20)
    a_age = models.IntegerField()
    book = models.ManyToManyField(to='Book')
