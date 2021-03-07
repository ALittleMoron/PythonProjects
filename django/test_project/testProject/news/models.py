from django.db import models


class Article(models.Model):
    """ Модель новостей. """
    title = models.CharField(max_length=150)
    context = models.TextField(blank=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    is_published = models.BooleanField(default=False)

