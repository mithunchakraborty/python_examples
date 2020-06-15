from django.db import models


class Articles(models.Model):
    pub_date = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=200, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Статью'
        verbose_name_plural = 'Статьи'