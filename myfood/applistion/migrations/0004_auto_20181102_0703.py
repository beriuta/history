# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-02 07:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('applistion', '0003_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='book',
        ),
        migrations.DeleteModel(
            name='Author',
        ),
        migrations.DeleteModel(
            name='Book',
        ),
    ]