#coding:utf-8
from __future__ import unicode_literals

from django.db import models

class Posting(models.Model):
    name = models.CharField(max_length=64,verbose_name='名前',help_text='名前を入力してください')
    message = models.CharField(max_length=255, verbose_name='メッセージ', help_text='メッセージを入力してください')
    created_at = models.DateTimeField(auto_now_add = True, verbose_name='投稿日時')
