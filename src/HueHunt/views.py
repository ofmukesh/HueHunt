from django.views import View
from django.conf import settings
from account.models import Account
from django.shortcuts import render
from live_game.models import LiveGame
from user_game.models import UserGame


# Custom 404 page
def custom_404(request, exception):
    return render(request, '404.html', status=404)


# Home page view
class Index(View):
    def get(self, request):
        user = request.user
        account = Account.objects.get(user=user)
        matches_played = account.matches_played
        matches_won = account.matches_won
        live_games = LiveGame.objects.filter(status='ongoing')
        old_games = UserGame.objects.filter(
            user=account, game__status='completed')

        context = {
            'matches_played': matches_played,
            'matches_won': matches_won,
            'live_games': live_games,
            'old_games': old_games,
            'debug': settings.DEBUG,
        }
        return render(request, 'home.html', context)
