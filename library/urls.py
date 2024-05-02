# library/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('authors/', views.author_list, name='author_list'),
    path('authors/<int:pk>/', views.author_detail, name='author_detail'),
    path('authors/new/', views.author_create, name='author_create'),
    # Define similar URL patterns for books.
]

# library_project/urls.py
from django.urls import include, path

urlpatterns = [
    path('', include('library.urls')),
]
