# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-26 15:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applition', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pulisher',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('p_name', models.CharField(max_length=20)),
            ],
        ),
    ]
