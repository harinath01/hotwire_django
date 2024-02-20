import http

from django.shortcuts import render, redirect, get_object_or_404
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


def update_view(request, pk):
    instance = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()

            messages.success(request, 'Task update successfully')
            return redirect(reverse('tasks:detail', kwargs={'pk': instance.pk}))

        status = http.HTTPStatus.UNPROCESSABLE_ENTITY
    else:
        status = http.HTTPStatus.OK
        form = TaskForm(instance=instance)

    return render(request, 'tasks/update.html', {'form': form}, status=status)


def detail_view(request, pk):
    instance = get_object_or_404(Task, pk=pk)

    return render(request, 'tasks/detail.html', {'task': instance})


def delete_view(request, pk):
    instance = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        instance.delete()

        messages.success(request, 'Task deleted successfully')
        return redirect('tasks:list')

    return render(request, 'tasks/delete.html', {'instance': instance})