from django.db import models


class DataBase(models.Model):
    title = models.CharField('Заголовок', max_length=50, default='Заголовок не указан')
    intro = models.CharField('Анонс', max_length=200)
    full_text = models.TextField('Текст статьи', max_length=5000)
    date = models.DateTimeField('Дата публикации')
    author = models.CharField('Автор статьи', max_length=50)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
