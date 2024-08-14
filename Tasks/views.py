# Create your views here.

from django.shortcuts import render, get_object_or_404, redirect
from .models import Task
from .forms import TaskForm
from django.contrib import messages

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'task_list.html', {'tasks': tasks})

def task_detail(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    return render(request, 'task_detail.html', {'task': task})

def task_create(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Task added successfully.')
            return redirect('task_list')
        else:
            messages.error(request, 'Error adding task. Please check the form for errors.')
    else:
        form = TaskForm()
    return render(request, 'task_form.html', {'form': form})

def task_edit(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request,'Task edited successfully.')
            return redirect('task_list')
        else:
            messages.error(request, 'Error editing task. Please check the form for errors.')
    else:
        form = TaskForm(instance=task)
    return render(request, 'task_form.html', {'form': form})

def task_delete(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    if request.method == "POST":
        task.delete()
        return redirect('task_list')
    return render(request, 'task_confirm_delete.html', {'task': task})

def task_filter(request, priority):
    tasks = Task.objects.filter(priority=priority)
    return render(request, 'task_list.html', {'tasks': tasks})
