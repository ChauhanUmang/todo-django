from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from todo.models import Task


def addTask(request):
    added_task = request.POST['added_task']
    Task.objects.create(task=added_task)
    return redirect('home')


def mark_as_done(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    task.is_completed = True
    task.save()
    return redirect("home")
