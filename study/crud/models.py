#coding:utf-8
from __future__ import unicode_literals

from django.db import models

class Message(models.Model):
    message = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True) #auto_now_add オブジェクトが生成された時の時刻を自動で設定する。
    updated_at = models.DateTimeField(auto_now = True )  #auto_now オブジェクトが保存された時の時刻を自動で設定する。

    def __str__(self):
        return u"{0}:{1}... ".format(self.id, self.message[:10])

