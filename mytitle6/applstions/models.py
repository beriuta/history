from django.db import models


# from django.contrib.auth.models import AbstractUser
# Create your models here.


# 班级表
class Class(models.Model):
    id = models.AutoField(primary_key=True)
    c_name = models.CharField(max_length=20)


# 学生表，一对多
class Student(models.Model):
    id = models.AutoField(primary_key=True)
    s_name = models.CharField(max_length=20)
    class_name = models.ForeignKey(to='Class')


# 老师班级表，多对多
class Teacher(models.Model):
    id = models.AutoField(primary_key=True)
    t_name = models.CharField(max_length=20)
    class_name = models.ManyToManyField(to='Class')
