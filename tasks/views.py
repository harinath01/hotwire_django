import http

from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse

from .forms import TaskForm
from tasks.models import Task


def create_view(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, 'Task created successfully')
            return redirect(reverse('tasks:list'))

        status = http.HTTPStatus.UNPROCESSABLE_ENTITY
    else:
        status = http.HTTPStatus.OK
        form = TaskForm()

    return render(request, 'tasks/create.html', {'form': form}, status=status)


def list_view(request):
    tasks = Task.objects.all().order_by('-pk')

    return render(request, 'tasks/list.html', {"tasks": tasks})
