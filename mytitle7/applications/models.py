from django.db import models

# Create your models here.

GENDER_CHOICES = ((0, '男'), (1, '女'), (2, '保密'))
DEFAULT_GENDER = 2


class UserInfo(models.Model):
    username = models.CharField(max_length=12, unique=True)
    password = models.CharField(max_length=20)
    phone = models.CharField(max_length=11, unique=True)
    email = models.EmailField()
    gender = models.PositiveIntegerField(choices=GENDER_CHOICES, default=DEFAULT_GENDER)

    def __str__(self):
        return self.username
