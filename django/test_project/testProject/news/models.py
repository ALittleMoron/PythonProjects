from django.db import models


class Article(models.Model):
    """ Модель новостей. """
    title = models.CharField(max_length=150, verbose_name='Заголовок')
    content = models.TextField(blank=True, verbose_name='Контент')
    created_at = models.DateField(auto_now_add=True, verbose_name='Создано')
    updated_at = models.DateField(auto_now=True, verbose_name='Обновлено')
    is_published = models.BooleanField(default=False, verbose_name='Опубликовано')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, null=True)


    def __str__(self):
        return self.title


    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
        ordering = ['-created_at']


class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Наименование категории')
    
    
    def __str__(self):
        return self.title

    
    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ['title']