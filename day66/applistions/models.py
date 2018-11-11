from django.db import models


# Create your models here.
class MyClass(models.Model):
    c_name = models.CharField(max_length=12)

    def __str__(self):
        return self.c_name


class Student(models.Model):
    s_name = models.CharField(max_length=12)
    myclass = models.ForeignKey(to='MyClass')

    def __str__(self):
        return self.s_name


class Teacher(models.Model):
    t_name = models.CharField(max_length=12)
    myclass = models.ManyToManyField(to='MyClass')

    def __str__(self):
        return self.t_name


class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    content = models.CharField(max_length=255)
    push_time = models.DateTimeField(auto_now_add=True)
    pcommen = models.ForeignKey(to='Comment', null=True)

    def __str__(self):
        return self.content


class Employee(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    salary = models.IntegerField()
    province = models.CharField(max_length=20)
    dept = models.CharField(max_length=20)
