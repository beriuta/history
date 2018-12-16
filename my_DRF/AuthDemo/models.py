from django.db import models


# Create your models here.
class UserInfo(models.Model):
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=32)
    token = models.UUIDField(null=True, blank=True)  # UUIDField是一个随机字符串,注册的时候是没有的,登录的时候才会有
    CHOICES = ((1,'vip'),(2,'普通用户'),(3,'vvip'))
    type = models.IntegerField(choices=CHOICES,default=2)