from django.shortcuts import render, get_object_or_404
from .models import Enemy, Location
# Create your views here.

def landing(request):
    enemy = Enemy.objects.all()
    location = Location.objects.all()
    context = {'enemy': enemy, 'location': location}
    return render(request, 'users.html', context)

def enemy_profile(request, enemy_id):
    # TODO: Change url to enemy names rather then an id
    enemy = get_object_or_404(Enemy, id=enemy_id)
    context = {'enemy': enemy, 'title':f'{enemy.name} Combat profile'}
    return render(request,'profile.html', context)