from django.urls import path
from .views import HomeView, NewsByCategoryView, GetArticleView, AddArticleView, user_register, user_login, user_logout


urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('register', user_register, name='register'),
    path('login',  user_login,  name='login'),
    path('logout', user_logout,  name='logout'),
    path('category/<int:category_id>',
         NewsByCategoryView.as_view(), name='category'),
    path('article/<int:article_id>', GetArticleView.as_view(), name='article'),
    path('article/add-article', AddArticleView.as_view(), name="add_article"),
]
