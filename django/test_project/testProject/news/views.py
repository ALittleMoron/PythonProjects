from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView

from .models import Article, Category
from .forms import ArticleForm


class HomeView(ListView):
    model = Article
    template_name = 'news/news.html'
    context_object_name = 'news'


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Все новости'
        return context

    
    def get_queryset(self):
        return Article.objects.filter(is_published=True)


class NewsByCategoryView(HomeView):
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(id=self.kwargs['category_id'])
        return context


    def get_queryset(self):
        return Article.objects.filter(category_id = self.kwargs['category_id'], is_published=True)


class GetArticleView(DetailView):
    model = Article
    template_name = 'news/article.html'
    pk_url_kwarg = 'article_id'


class AddArticleView(CreateView):
    form_class = ArticleForm
    template_name = 'news/add_article.html'