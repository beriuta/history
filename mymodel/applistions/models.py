from django.db import models


# Create your models here.
class MyCharField(models.Field):
    def __init__(self, max_length, *args, **kwargs):
        super(MyCharField, self).__init__(max_length=max_length, *args, **kwargs)  # 重新写了父类的__init__方法
        # 在类的继承中，如果你想要重写父类的方法而不是覆盖的父类方法，这个时候我们可以使用super()方法来实现
        self.max_length = max_length

    def db_type(self, connection):
        """
        限定生成数据库表的字段类型为char，长度为max_length指定的值
        """
        return 'char(%s)' % self.max_length


class UserInfo(models.Model):
    name = MyCharField(max_length=12, null=True, default='张三')
    birthday = models.DateTimeField(verbose_name='生日', null=True)
    gender = models.SmallIntegerField(choices=((1, '男'), (2, '女'), (3, '保密')), default=3)

    def __str__(self):
        return '<userInfo' + self.name + '>'


class Blog(models.Model):
    title = models.CharField(max_length=32)
    push_tim = models.DateTimeField(auto_now_add=True)  # 发布时间，数据库中创建这条记录的时间
    edit_time = models.DateTimeField(auto_now=True)  # 最后修改的时间

    class Meta:
        db_table = 'biog'  # 控制建表的表名


class Site(models.Model):
    ip = models.GenericIPAddressField()
    port = models.IntegerField()

    class Meta:
        unique_together = (('ip', 'port'),)  # 一起唯一，可以ip单独的可以重复，port单独的可以重复，但是两个一起只能唯一


class Publisher(models.Model):
    id = models.AutoField(primary_key=True)
    p_name = models.CharField(max_length=20)
    address = models.CharField(max_length=50)
    date = models.DateField(null=True)


class Book(models.Model):
    b_name = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    coding = models.CharField(max_length=50,unique=True)
    publisher = models.ForeignKey(to='Publisher')


class author(models.Model):
    a_name = models.CharField(max_length=20)
    birthday = models.DateTimeField(verbose_name='生日', null=True)
    gender = models.SmallIntegerField(choices=((1, '女'), (2, '男'), (3, '保密')), default=1)
    phone_num = MyCharField(max_length=11, unique=True)
    email = models.CharField(max_length=20)
    book = models.ManyToManyField(to='Book')
