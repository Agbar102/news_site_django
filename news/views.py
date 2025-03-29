from django.shortcuts import render
from .models import Articles

def news(request):
    news = Articles.objects.order_by('-date')
    return render(request, 'news/news.html', {'news': news})

def create(request):
    return render(request, 'news/create.html')
