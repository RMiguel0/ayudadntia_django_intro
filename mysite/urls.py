from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import render
from flights import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('flights/', include('flights.urls')),
    path('booking/', include('booking.urls')),
    path('', lambda request: render(request, 'home.html'), name='home'),
    path('find/', views.search_pokemon, name='pokemon_search'),
]
