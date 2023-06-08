from django.shortcuts import render, redirect
from .models import DataBase
from .forms import DataBaseForm
from django.views.generic import DetailView, UpdateView, DeleteView


def news_home(request):
    news = DataBase.objects.order_by('date')
    return render(request, 'news/news_home.html', {'news': news})


class NewsDetailView(DetailView):
    model = DataBase
    template_name = 'news/news-detail.html'
    context_object_name = 'article'


class NewsUpdateView(UpdateView):
    model = DataBase
    template_name = 'news/create.html'
    form_class = DataBaseForm


class NewsDeleteView(DeleteView):
    model = DataBase
    success_url = '/news/'
    template_name = 'news/news-delete.html'


def create(request):
    error = ''
    if request.method == 'POST':
        form = DataBaseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма заполнена с ошибкой'
    form = DataBaseForm()
    data = {
        'form': form,
        'error': error,
    }
    return render(request, 'news/create.html', data)
