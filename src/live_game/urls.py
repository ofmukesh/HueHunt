
from django.urls import path
from .views import game_detail

urlpatterns = [
    path('game/<uuid:game_id>/', game_detail, name='game_detail'),
]
