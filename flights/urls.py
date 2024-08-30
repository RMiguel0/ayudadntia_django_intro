from django.urls import path
from . import views

app_name = 'flights'


urlpatterns = [
    path('', views.home, name='home'),
    path('pokemon/<str:pokemon_name>/', views.pokemon_detail, name='pokemon_detail'),
    path('search/', views.search_pokemon, name='pokemon_search'),
]