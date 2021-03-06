# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-08 13:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author2Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Author_2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Book_2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='author_2',
            name='book',
            field=models.ManyToManyField(through='my_app.Author2Book', to='my_app.Book_2'),
        ),
        migrations.AddField(
            model_name='author2book',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_app.Author_2'),
        ),
        migrations.AddField(
            model_name='author2book',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_app.Book_2'),
        ),
    ]
