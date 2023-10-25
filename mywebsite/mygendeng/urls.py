from django.urls import path
from . import views

urlpatterns = [
    path('mygendeng/', views.mygendeng, name='mygendeng'),
]