# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-28 14:16
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bookmarks', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bookmark',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
                ('bookmarks', models.ManyToManyField(to='bookmarks.Bookmark')),
            ],
        ),
        migrations.AddField(
            model_name='bookmark',
            name='link',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookmarks.Link'),
        ),
        migrations.AddField(
            model_name='bookmark',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
