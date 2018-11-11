"""
这是周末作业的表格
"""
from django.db import models


# Create your models here.
class Publisher2(models.Model):
    p_name = models.CharField(max_length=20)
    city = models.CharField(max_length=20)

    def __str__(self):
        return self.p_name


class Author(models.Model):
    a_name = models.CharField(max_length=20)
    age = models.IntegerField()
    companion_age = models.IntegerField(null=True)
    phone = models.CharField(max_length=11)
    detail = models.OneToOneField(to='AuthorInfo')

    def __str__(self):
        return self.a_name


class AuthorInfo(models.Model):
    addr = models.CharField(max_length=60)
    email = models.EmailField()


class Book(models.Model):
    title = models.CharField(max_length=20)
    pub_date = models.DateField(auto_now_add=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    memo = models.TextField(null=True)  # 备忘录
    # 创建外键，关联出版社
    publisher = models.ForeignKey(to='Publisher2')
    author = models.ManyToManyField(to='Author')

    def __str__(self):
        return self.title
