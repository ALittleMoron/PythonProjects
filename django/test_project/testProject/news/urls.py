from django.urls import path
from .views import index, get_category, get_article

urlpatterns = [
    path('', index, name='index'),
    path('category/<int:category_id>', get_category, name='category'),
    path('article-<int:article_id>', get_article, name='article'),
]