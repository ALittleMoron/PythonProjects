from django.urls import path
from .views import HomeView, NewsByCategoryView, GetArticleView, AddArticleView


urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('category/<int:category_id>', NewsByCategoryView.as_view(), name='category'),
    path('article/<int:article_id>', GetArticleView.as_view(), name='article'),
    path('article/add-article', AddArticleView.as_view(), name="add_article"),
]