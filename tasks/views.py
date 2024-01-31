from django.shortcuts import render, redirect

from .forms import TaskForm


def create_view(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('/')
    else:
        form = TaskForm()

    return render(request, 'tasks/create.html', {'form': form})