from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django import forms
from .models import Task
from .forms import TaskForm


# Create your views here.
def index(request):
    tasks = Task.objects.all()
    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    return render(request, 'tasks/list.html', {'tasks': tasks, 'form': form})


def update(request, id):
    task = Task.objects.get(pk=id)
    form = TaskForm(instance=task,  page=True)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)

        if form.is_valid():
            form.save()
        return redirect('/')

    return render(request, 'tasks/update.html', {'task': task, 'form': form})


def delete(request, id):
    task = Task.objects.get(pk=id)
    if request.method == 'POST':
        task.delete()
        return redirect('/')

    return render(request, 'tasks/delete.html', {'task': task})
