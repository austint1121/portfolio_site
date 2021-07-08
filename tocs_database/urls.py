from . import views
from django.urls import path

app_name = 'tocs_database'

urlpatterns = [
    path('', views.landing, name='landing'),
    path('<str:enemy_name>/', views.enemy_profile)
]