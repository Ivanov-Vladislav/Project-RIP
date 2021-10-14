from django.db import models

# Create your models here.

class Articles11(models.Model):
    article_title = models.CharField('Название книги', max_length= 50)
    article_author = models.CharField('автор', max_length= 30)
    article_text = models.TextField('описание книги')
    date = models.CharField('Дата выхода', max_length= 10)
    avatar = models.ImageField(null=True, blank=True, upload_to="images/")


    def __str__(self):
        return self.article_title

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
