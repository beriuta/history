from django.db import models


# 这是出版社表格
# Create your models here.
class Publisher(models.Model):
    name = models.CharField(max_length=12)
    city = models.CharField(max_length=12)
    birthday = models.DateField(auto_now_add=True)
    ceo = models.CharField(max_length=12)
