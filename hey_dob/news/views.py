from django.shortcuts import render, redirect
from .models import DataBase
from .forms import DataBaseForm


def news_home(request):
    news = DataBase.objects.order_by('date')
    return render(request, 'news/news_home.html', {'news': news})


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
