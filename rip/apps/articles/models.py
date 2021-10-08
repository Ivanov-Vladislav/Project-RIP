from django.db import models

# Create your models here.

class Article(models.Model):
    article_title = models.CharField('Название книги', max_length= 50)
    article_text = models.TextField('описание книги')

    def __str__(self):
        return self.article_title

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
