#coding:utf-8
from django.shortcuts import render
from django.http.response import HttpResponse
from django.views.generic import TemplateView
from forms import StudyForm
from datetime import datetime
from django.shortcuts import get_object_or_404, render_to_response
# Create your views here.


"""
def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs) # はじめに継承元のメソッドを呼び出す
    context["foo"] = "bar"
    return context
"""


def form(request):
    form = StudyForm()
    if form.is_valid():
        message = "データの検証に成功しました。"
    else:
        message = "データの検証に失敗しました。"
    context = {
        "form":form,
        'message' : message,
    }
    return render(request,"mysite/index.html",context )

