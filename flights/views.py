from django.shortcuts import render, redirect
import requests, os
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse, JsonResponse



# Create your views here.


def home(request):
    return render(request,'flights_page.html')

def pokemon_detail(request, pokemon_name):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}/"
    response = requests.get(url)
    
    if response.status_code == 200:
        pokemon_data = response.json()
        return render(request, 'pokemon_detail.html', {'pokemon': pokemon_data})
    else:
        return render(request, 'pokemon_not_found.html', {'pokemon_name': pokemon_name})
    
def search_pokemon(request):
    pokemon_data = None
    error = None

    if 'pokemon_name' in request.GET:
        pokemon_name = request.GET['pokemon_name'].lower()
        url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}/"
        response = requests.get(url)
        
        if response.status_code == 200:
            pokemon_data = response.json()
        else:
            error = 'Pokémon not found'

    return render(request, 'flights_page.html', {'pokemon': pokemon_data, 'error': error})