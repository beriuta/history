# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-09 02:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('content', models.CharField(max_length=255)),
                ('push_time', models.DateTimeField(auto_now_add=True)),
                ('pcommen', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='applistions.Comment')),
            ],
        ),
    ]