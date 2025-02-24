from django.urls import path
from . import views

app_name = 'ligtas_ani'

urlpatterns = [
    path('', views.index, name='index'),
    path('add_location/', views.add_location, name='add_location'),
]