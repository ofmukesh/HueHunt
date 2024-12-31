from celery import shared_task
from .models import LiveGame
from game_profile.models import GameProfile
from django.utils import timezone


@shared_task
def manage_live_games():
    # Complete ongoing live games
    ongoing_games = LiveGame.objects.filter(status='ongoing')
    for game in ongoing_games:
        game.status = 'completed'
        game.end_time = timezone.now()
        game.save()

    # Create new live game
    game_profiles = GameProfile.objects.filter(is_active=True)
    for profile in game_profiles:
        LiveGame.objects.create(game_profile=profile, status='ongoing')
