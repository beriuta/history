# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-06 11:43
from __future__ import unicode_literals

import applistions.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', applistions.models.MyCharField(default='张三', max_length=12, null=True)),
                ('birthday', models.DateTimeField(null=True, verbose_name='生日')),
                ('gender', models.SmallIntegerField(choices=[(1, '男'), (2, '女'), (3, '保密')], default=3)),
            ],
        ),
    ]
