from django.db import models


# Create your models here.
class Book_2(models.Model):
    title = models.CharField(max_length=20)


class Author_2(models.Model):
    name = models.CharField(max_length=20)
    # 手动创建第三张表，through定义第三张表名，through_fields定义表中的字段,因为book字段定义在Author——2类中，
    # 所以through_fields里面的 源 就是‘author’ 目标 就是‘book’
    book = models.ManyToManyField(to='Book_2', through='Author2Book', through_fields=('author', 'book'))


class Author2Book(models.Model):
    author = models.ForeignKey(to='Author_2')
    book = models.ForeignKey(to='Book_2')
    score = models.IntegerField(null=True)

    class Mate:
        unique_together = (('author', 'book'),)
