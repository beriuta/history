from django.db import models


# Create your models here.
class Publisher(models.Model):
    name = models.CharField(max_length=50)


class Auther(models.Model):
    name = models.CharField(max_length=50)
    age = models.CharField(max_length=5)
    books = models.ManyToManyField(to='Book')


class Book(models.Model):
    name = models.CharField(max_length=100)
    publisher = models.ForeignKey(to='Publisher')
