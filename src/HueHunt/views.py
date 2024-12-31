from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from live_game.models import LiveGame
from account.models import Account
from user_game.models import UserGame
from django.contrib.auth import logout


class CustomLoginView(LoginView):
    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('/')
        return super().dispatch(request, *args, **kwargs)


def custom_404(request, exception):
    return render(request, '404.html', status=404)


def home_view(request):
    user = request.user
    account = Account.objects.get(user=user)
    matches_played = account.matches_played
    matches_won = account.matches_won
    live_games = LiveGame.objects.filter(status='ongoing')
    old_games = UserGame.objects.filter(user=account, game__status='completed')

    context = {
        'matches_played': matches_played,
        'matches_won': matches_won,
        'live_games': live_games,
        'old_games': old_games,
    }
    return render(request, 'home.html', context)


def forgot_password(request):
    return render(request, 'forgot_password.html')
