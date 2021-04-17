from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import login, logout

from .models import Article, Category
from .forms import ArticleForm, CustomUserCreationForm, CustomAuthenticationForm


def user_register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Вы зарегистрировались')
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = CustomUserCreationForm()
    return render(request, 'news/register.html', {'form': form})


def user_login(request):
    if request.method == "POST":
        form = CustomAuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'Вы вошли в систему')
            return redirect('index')
        else:
            messages.error(request, 'Ошибка входа')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'news/login.html', {'form': form})


def user_logout(requeset):
    logout(requeset)
    return redirect('index')


class HomeView(ListView):
    model = Article
    template_name = 'news/news.html'
    context_object_name = 'news'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Все новости'
        return context

    def get_queryset(self):
        return Article.objects.filter(is_published=True).select_related('category')


class NewsByCategoryView(HomeView):
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(id=self.kwargs['category_id'])
        return context

    def get_queryset(self):
        return Article.objects.filter(category_id=self.kwargs['category_id'], is_published=True).select_related('category')


class GetArticleView(DetailView):
    model = Article
    template_name = 'news/article.html'
    pk_url_kwarg = 'article_id'


class AddArticleView(CreateView):
    form_class = ArticleForm
    template_name = 'news/add_article.html'
