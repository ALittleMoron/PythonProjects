from django.urls import path
from .views import index, get_news_by_category, get_article, add_article

urlpatterns = [
    path('', index, name='index'),
    path('category/<int:category_id>', get_news_by_category, name='category'),
    path('article/<int:article_id>', get_article, name='article'),
    path('article/add-article', add_article, name="add_article"),
]