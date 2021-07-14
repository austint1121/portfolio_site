from django.shortcuts import render, get_object_or_404
from .models import Enemy, Location
# Create your views here.

def landing(request):
    enemy = Enemy.objects.all()
    location = Location.objects.all()
    context = {'enemy': enemy, 'location': location}
    return render(request, 'users.html', context)

def enemy_profile(request, enemy_name):
    enemy = get_object_or_404(Enemy, name=enemy_name)
    earth = int(enemy.earth_efficacy/2)
    water = int(enemy.water_efficacy / 2)
    fire = int(enemy.fire_efficacy / 2)
    wind = int(enemy.wind_efficacy / 2)
    context = {'enemy': enemy, 'title':f'{enemy.name} Combat profile', 'earth': earth, 'water': water, 'fire': fire, 'wind': wind,}
    if enemy.time_efficacy:
        time = int(enemy.time_efficacy / 2)
        space = int(enemy.space_efficacy / 2)
        mirage = int(enemy.mirage_efficacy / 2)
        context['time'] = time
        context['space'] = space
        context['mirage'] = mirage
    return render(request,'profile.html', context)