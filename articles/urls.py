from django.urls import path
from . import views


app_name = 'articles'

urlpatterns = [
    path('list/', views.article_list, name='list'),
    path('create/', views.article_create, name='create'),
    path('articles/detail/<int:post_id>/', views.article_detail, name='articles_detail'),
    path('category/<str:category>/', views.article_by_category, name='article_by_category'),
]