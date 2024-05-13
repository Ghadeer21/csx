from django.urls import path
from . import views

urlpatterns = [
   # path('', views.example_view, name='example-view'),
    # Add other URL patterns as needed
     path('', views.header, name='header'),
     path('list', views.listbooks, name='listbooks'),
     path('model', views.model, name='model'),
     path('books', views.books, name='books'),
     path('we', views.we, name='we'),
     path('display_books', views.display_books, name='display_books'),
     path('search_books', views.search_books, name='search_books'),
    
   
]
#example/