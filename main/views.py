from django.shortcuts import render

def index(request):
    date = {
        'title': 'Главная страница'
    }
    return render(request, 'main/index.html', date)

def about(request):
    return render(request, 'main/about.html')

