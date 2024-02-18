from django.urls import path
from . import views

urlpatterns = [
   # path('', views.example_view, name='example-view'),
    # Add other URL patterns as needed
     path('', views.header, name='header'),
     
]
#example/