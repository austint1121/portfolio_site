from django.shortcuts import render, get_object_or_404
from .models import Enemy, Location
# Create your views here.

def landing(request):
    enemy = Enemy.objects.all()
    location = Location.objects.all()
    context = {'enemy': enemy, 'location': location}
    return render(request, 'users.html', context)

def enemy_profile(request, location_name, enemy_name):
    enemy = get_object_or_404(Enemy, name=enemy_name)
    earth = int(enemy.earth_efficacy/2)
    water = int(enemy.water_efficacy / 2)
    fire = int(enemy.fire_efficacy / 2)
    wind = int(enemy.wind_efficacy / 2)
    context = {'enemy': enemy, 'location_name': location_name, 'title':f'{enemy.name} Combat Profile', 'earth': earth, 'water': water, 'fire': fire, 'wind': wind,}
    if enemy.time_efficacy:
        time = int(enemy.time_efficacy / 2)
        space = int(enemy.space_efficacy / 2)
        mirage = int(enemy.mirage_efficacy / 2)
        context['time'] = time
        context['space'] = space
        context['mirage'] = mirage
    return render(request,'profile.html', context)

def location_view(request, location_name):
    location = get_object_or_404(Location, name=location_name)
    enemies_in_location = Enemy.objects.all()
    context = {'enemy': enemies_in_location, 'location': location, 'title':f'{location_name} Area Profile'}
    return render(request, 'locations.html', context)