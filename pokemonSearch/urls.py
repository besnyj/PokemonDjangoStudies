from django.urls import path
from . import views

urlpatterns = [
    path('', views.frontpage, name='frontpage'),
    path('pokemon/', views.pokemonSearch, name='pokemon'),
]
