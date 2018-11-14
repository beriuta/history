from django.db import models

# Create your models here.


class UserInfo(models.Model):
    name = models.CharField(max_length=20)
    password = models.CharField(max_length=20)


class Publisher(models.Model):
    pname = models.CharField(max_length=20)
    addr = models.TextField(null=True)