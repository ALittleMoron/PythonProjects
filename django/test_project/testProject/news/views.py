from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from .models import Article, Category
from .forms import ArticleForm


def index(request):
    content = {
        'title': 'Все новости',
        'news': Article.objects.all(),
    }
    return render(request, 'news/news.html', content)


def get_news_by_category(request, category_id):
    content = {
        'title': Category.objects.get(id=category_id),
        'news': Article.objects.filter(category_id=category_id, is_published=True),
    }
    return render(request, 'news/news.html', content)


def get_article(request, article_id):
    content = {
        'article': get_object_or_404(Article, pk=article_id),
    }
    return render(request, 'news/article.html', content)


def add_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect(article)

    else:
        form = ArticleForm()
    return render(request, 'news/add_article.html', {'form': form})