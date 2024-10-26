from django.urls import path

from book import views

app_name = 'books'

urlpatterns = [
    path('authors/', views.author_list_create name='author_list_create')
]