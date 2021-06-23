from django.shortcuts import render
from .models import Enemy, Location
# Create your views here.

def landing(request):
    enemy = Enemy.objects.all()
    location = Location.objects.all()
    context = {'enemy': enemy, 'location': location}
    return render(request, 'users.html', context)