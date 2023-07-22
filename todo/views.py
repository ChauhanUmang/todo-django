from django.http import HttpResponse
from django.shortcuts import render, redirect

from todo.models import Task


def addTask(request):
    added_task = request.POST['added_task']
    Task.objects.create(task=added_task)
    return redirect('home')
