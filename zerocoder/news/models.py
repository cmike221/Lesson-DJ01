from django.db import models

# Create your models here.
class News_post(models.Model):
    title = models.CharField('Название новости', max_length=50)
    short_description = models.CharField('Кратное описание новости', max_length=200)  # можно до 256
    text = models.TextField('Новость')
    pub_date = models.DateTimeField('Дата публикации')
    # author = models.

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
