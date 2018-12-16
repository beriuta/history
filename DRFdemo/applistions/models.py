from django.db import models

__all__ = ['Student','Class','Teacher']

CHOICES = ((1,'男'),(2,'女'))
# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=32)
    age = models.IntegerField()
    student_id = models.IntegerField()
    on_class_time = models.DateField(null=True)
    c_num = models.ForeignKey(to='Class', null=True)


class Class(models.Model):
    c_name = models.CharField(max_length=32)
    teacher = models.ManyToManyField(to='Teacher')


class Teacher(models.Model):
    t_name = models.CharField(max_length=32)
    sex = models.IntegerField(choices=CHOICES,null=True)