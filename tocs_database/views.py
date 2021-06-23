from django.shortcuts import render
from .models import Enemy
# Create your views here.

def landing(request):
    enemy = Enemy.objects.all()
    context = {'enemy': enemy}
    return render(request, 'users.html', context)