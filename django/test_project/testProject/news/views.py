from django.http import HttpResponse
from django.shortcuts import render

from .models import Article, Category


def index(request):
    content = {
        'title': 'Все новости',
        'news': Article.objects.all(),
        'categories': Category.objects.all(),
    }
    return render(request, 'news/news.html', content)


def get_category(request, category_id):
    content = {
        'title': Category.objects.get(id=category_id),
        'news': Article.objects.filter(category_id=category_id, is_published=True),
        'categories': Category.objects.all(),
    }
    return render(request, 'news/news.html', content)