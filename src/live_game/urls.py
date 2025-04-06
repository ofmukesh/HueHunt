
from django.urls import path
from .views import game_detail, complete_manual_game

urlpatterns = [
    path('game/<uuid:game_id>/', game_detail, name='game_detail'),
    path("game/<uuid:game_id>/complete_manual_game/<str:result>/", complete_manual_game, name="complete_manual_game"),
]
