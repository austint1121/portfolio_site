from . import views
from django.urls import path

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('success/', views.email_success, name='success'),
    path('about_me/', views.about_me, name='success'),

]