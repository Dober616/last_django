from .models import DataBase
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea


class DataBaseForm(ModelForm):
    class Meta:
        model = DataBase
        fields = ['title', 'intro', 'full_text', 'date', 'author']

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название статьи',
            }),
            'intro': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Анонс статьи',
            }),
            'date': DateTimeInput(attrs={
                'class': 'form-control',
            }),
            'full_text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Текст статьи',
            }),
            'author': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Автор статьи',
            }),
        }
