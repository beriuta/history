# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-08 09:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('a_name', models.CharField(max_length=20)),
                ('gender', models.SmallIntegerField(choices=[(1, '女'), (2, '男'), (3, '保密')], default=3)),
                ('phone', models.CharField(max_length=11, unique=True)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='AuthorInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('birthday', models.DateField()),
                ('city', models.CharField(max_length=20)),
                ('is_mary', models.BooleanField()),
                ('income', models.BigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('b_name', models.CharField(max_length=20)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('isbn', models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_name', models.CharField(max_length=20)),
                ('addr', models.TextField()),
                ('timp', models.DateField()),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='publisher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books', to='applistions.Publisher'),
        ),
        migrations.AddField(
            model_name='author',
            name='books',
            field=models.ManyToManyField(related_name='authors', to='applistions.Book'),
        ),
        migrations.AddField(
            model_name='author',
            name='info',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='applistions.AuthorInfo'),
        ),
    ]