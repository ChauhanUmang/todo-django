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


def mark_as_undone(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    task.is_completed = False
    task.save()
    return redirect('home')


def edit_task(request, task_id):
    get_task = get_object_or_404(Task, pk=task_id)
    if request.method == "POST":
        updated_task = request.POST['updated_task']
        get_task.task = updated_task
        get_task.save()
        return redirect("home")
    else:
        context = {
            'get_task': get_task
        }
        return render(request, 'edit_task.html', context)


def delete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    task.delete()
    return redirect("home")
