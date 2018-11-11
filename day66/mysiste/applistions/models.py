from django.db import models


# 这是班级，学生，老师表
# Create your models here.
class MyClass(models.Model):
    c_name = models.CharField(max_length=20)

    def __str__(self):
        return self.c_name


class Student(models.Model):
    s_name = models.CharField(max_length=20)
    my_class = models.ForeignKey(to='MyClass')

    def __str__(self):
        return self.s_name


class Teacher(models.Model):
    t_name = models.CharField(max_length=20)
    my_class = models.ManyToManyField(to='MyClass')

    def __str__(self):
        return self.t_name
