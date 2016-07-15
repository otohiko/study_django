#coding:utf-8
from django import forms

class MessageForm(forms.Form):
    message = forms.CharField(label='メッセージ', max_length=100, required=True)