# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-07-14 14:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Posting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='\u540d\u524d\u3092\u5165\u529b\u3057\u3066\u304f\u3060\u3055\u3044', max_length=64, verbose_name='\u540d\u524d')),
                ('message', models.CharField(help_text='\u30e1\u30c3\u30bb\u30fc\u30b8\u3092\u5165\u529b\u3057\u3066\u304f\u3060\u3055\u3044', max_length=255, verbose_name='\u30e1\u30c3\u30bb\u30fc\u30b8')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='\u6295\u7a3f\u65e5\u6642')),
            ],
        ),
    ]