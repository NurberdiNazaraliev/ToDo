from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods

from . import views
from .models import ToDo
from .forms import ToDoForm


# Create your views here.
def home(request):
    todos = ToDo.objects.all()
    return render (request, "todolist/index.html", {"todos": todos, 'title': "Homepage"})


@require_http_methods(['POST'])
def add(request):
    title = request.POST['title']
    description = request.POST['description']
    todo = ToDo(title=title, description=description)
    todo.save()
    return redirect('home')


def update(request, todo_id):
    todo = ToDo.objects.get(id=todo_id)
    todo.is_complete = not todo.is_complete
    todo.save()
    return redirect('home')

def delete(request, todo_id):
    todo = ToDo.objects.get(id=todo_id)
    todo.delete()
    return redirect('home')




def edit(request, todo_id):
    todo = ToDo.objects.get(id=todo_id)

    if request.method == 'POST':
        form = ToDoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ToDoForm(instance=todo)

    return render(request, 'todolist/edit.html', {'form': form, 'todo': todo, 'title': 'Edit Task'})


