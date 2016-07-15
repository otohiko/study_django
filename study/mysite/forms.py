#coding:utf-8
from django import forms

class StudyForm(forms.Form):
    name = forms.CharField(label='名前', max_length=20,required=True)
    phone_number = forms.CharField(label='電話番号', max_length=20, required=True)


class MessageForm(forms.Form):
    message = forms.CharField(label='メッセージ', max_length=100, required=True)