from . import views
from django.urls import path

app_name = 'tocs_database'

urlpatterns = [
    path('', views.landing, name='landing'),
    path('<str:location_name>/<str:enemy_name>/', views.enemy_profile),
    path('<str:location_name>/', views.location_view)
]