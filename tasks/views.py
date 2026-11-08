from django.shortcuts import render, redirect
from .models import Task

def home(request):

    if request.method == "POST":

        title = request.POST.get('title')
        description = request.POST.get('description')

        Task.objects.create(
            title=title,
            description=description
        )
        return redirect('home')

    tasks = Task.objects.all()
    pending_count = Task.objects.filter(completed=False).count()

    completed_count = Task.objects.filter(completed=True).count()

    return render(request, 'tasks/home.html', {
    'tasks': tasks,
    'pending_count': pending_count,
    'completed_count': completed_count
    })

def complete_task(request, id):

    task = Task.objects.get(id=id)

    task.completed = True

    task.save()

    return redirect('home')

def delete_task(request, id):

    if request.method == "POST":
        task = Task.objects.get(id=id)
        task.delete()

    return redirect('home')

def edit_task(request, id):

    task = Task.objects.get(id=id)

    if request.method == "POST":
        task.title = request.POST.get('title')
        task.description = request.POST.get('description')
        task.save()

        return redirect('home')

    return render(request, 'tasks/edit.html', {'task': task})