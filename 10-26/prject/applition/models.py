from django.db import models


# 用户表
class UserInfo(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=20)
    password = models.CharField(max_length=30)


# 出版社表
class Publisher(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name  # 当只有打印这个对象本身时才会触发__str__
