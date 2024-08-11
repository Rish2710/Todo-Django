from django.shortcuts import render
from todos.models import Task

def home(request):
    tasks = Task.objects.filter(is_completed = False).order_by('-updated_at')
    
    completd_task =  Task.objects.filter(is_completed = True)
    context = {
        "tasks": tasks,
        'completed_tasks': completd_task,
    }
    return render(request, 'home.html', context)