from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.http import Http404
from .models import ToDo

def index(request):
    todos = ToDo.objects.all()
    return  render(request, 'todoap/index.html', {'todo_list': todos, 'title': 'Главная страница'})

@require_http_methods(['POST'])
@csrf_exempt
def add(request):
    title = request.POST['title']
    todo = ToDo(title=title)
    todo.save()
    return redirect('index')

def update(request, todo_id):
    try:
        todo = ToDo.objects.get(id=todo_id)
    except ToDo.DoesNotExist:
        raise Http404("Задача не найдена")
    todo.is_complete = not todo.is_complete
    todo.save()
    return redirect('index')


def delete(request, todo_id):
    try:
        todo = ToDo.objects.get(id=todo_id)
    except ToDo.DoesNotExist:
        raise Http404("Задача не найдена")
    todo.delete()
    return redirect('index')

