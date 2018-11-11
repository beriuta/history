from django.db import models


# Create your models here.
class Publisher(models.Model):
    p_name = models.CharField(max_length=20)
    addr = models.TextField()
    timp = models.DateField()  # 只有年月日


class Book(models.Model):
    b_name = models.CharField(max_length=20)
    # 价格总数字是六位数，其中小数点后面两位数
    price = models.DecimalField(max_digits=6, decimal_places=2)
    isbn = models.CharField(max_length=20, unique=True)
    # on_delete关联删除，在这个表格中删除，另一个表格的相应内容也删除，related_name属性是重命名
    publisher = models.ForeignKey(to='Publisher', on_delete=models.CASCADE, related_name='books')


class Author(models.Model):
    GENDER_CHOICE = (
        (1, '女'),
        (2, '男'),
        (3, '保密'),
    )
    a_name = models.CharField(max_length=20)
    gender = models.SmallIntegerField(choices=GENDER_CHOICE, default=3)
    phone = models.CharField(max_length=11, unique=True)
    email = models.EmailField()
    # 多对多关联书籍
    books = models.ManyToManyField(to='Book', related_name='authors')
    # 详细信息在另一个表格中
    info = models.OneToOneField(to='AuthorInfo')


class AuthorInfo(models.Model):
    # 生日对应Python中的datetime.datetime日期
    birthday = models.DateField()
    city = models.CharField(max_length=20)
    is_mary = models.BooleanField()
    income = models.BigIntegerField()
