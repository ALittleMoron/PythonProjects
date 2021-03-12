from django.http import HttpResponse
from django.shortcuts import render

from .models import Article


def index(request):
    news = Article.objects.all()
    return render(request, 'news/index.html', {'news': news, 'title': 'Все новости'})