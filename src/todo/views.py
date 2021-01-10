from django.shortcuts import render
from .models import Todo
from .forms import TodoAddForm

# Create your views here.

def home(request):
    return render(request, "todo/home.html")

def todo_list(request):
    todos = Todo.objects.all()
    context = {
        'todos': todos
    }
    return render(request, "todo/todo_list.html", context)

def todo_create(request):
    form = TodoAddForm()
    context = {
        'form': form
    }
    return render(request, "todo/todo_create.html", context)