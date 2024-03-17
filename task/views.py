from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UpdateTaskForm
from .models import Task

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'task_list.html', {'tasks': tasks})

@login_required
def my_view(request):
    if request.method == 'POST':
        form = UpdateTaskForm(request.POST)
        if form.is_valid():
            task_id = form.cleaned_data['task_id']
            task = Task.objects.get(id=task_id)
            task.title = form.cleaned_data['title']
            task.description = form.cleaned_data['description']
            task.deadline = form.cleaned_data['deadline']
            task.save()
            return HttpResponseRedirect('/success/')  
    else:
        form = UpdateTaskForm()
    return render(request, 'task_list.html', {'form': form})

def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    messages.success(request, 'La tarea se eliminó correctamente.')
    return HttpResponseRedirect('/')

def complete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.completed = True
    task.save()
    messages.success(request, 'La tarea se marcó como completada.')
    return HttpResponseRedirect('/')
