from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm
from django.views.generic import DetailView, UpdateView, DeleteView

def news(request):
    news = Articles.objects.order_by('-date')
    return render(request, 'news/news.html', {'news': news})

class NewsDetailView(DetailView):
    model = Articles
    template_name = 'news/details_view.html'
    context_object_name = 'article'


class NewsUpdateViews(UpdateView):
    model = Articles
    template_name = 'news/create.html'

    form_class = ArticlesForm


class NewsDeleteViews(DeleteView):
    model = Articles
    success_url = '/news/'
    template_name = 'news/create.html'


def create(request):
    error = ''
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news')
        else:
            error = 'Форма была не верной'

    form = ArticlesForm()

    date = {
        'form': form,
        'error': error
    }
    return render(request, 'news/create.html', date)
