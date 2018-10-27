from django.db import models


# Create your models here.
class Info(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=30)  # 创建数据库的时候出了一个错，APP包里的创建数据库的日志跟数据库里面对不上


# 创建出版社数据库表格
class Pulisher(models.Model):
    id = models.AutoField(primary_key=True)
    p_name = models.CharField(max_length=20)


