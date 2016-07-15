#coding:utf-8
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Message
from .forms import MessageForm
from django.views.decorators.http import require_POST


def index(request):
    path = 1
    context = {
        'messages' : Message.objects.all(),
    }
    return render(request, 'crud/index.html', context)

def add(request):
    message_form = MessageForm(request.POST)
    if message_form.is_valid():
        Message.objects.create(**message_form.cleaned_data)
        return redirect('crud:index')
    context = {
        'message_form': message_form,
    }
    return render(request, 'crud/edit.html',context)


def edit(request, edit_id):
    message = get_object_or_404(Message, id = edit_id)
    if request.method == 'POST':
        message_form = MessageForm(request.POST)
        if message_form.is_valid():
            message.message = message_form.cleaned_data['message']
            message.save()
            return redirect('crud:index')
    else:
         message_form = MessageForm({ 'message' : message })
    context = {
        'message_form' : message_form,
    }
    return render(request, 'crud/edit.html',context )


def delete(request):
    delete_ids = request.POST.getlist('delete_ids')
    if delete_ids:
        Message.objects.filter(id__in = delete_ids).delete()
    return redirect('crud:index')
