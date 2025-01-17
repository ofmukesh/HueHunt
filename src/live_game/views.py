from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from .models import LiveGame
from user_game.models import UserGame
from .forms import BetForm
from account.models import Account as Acc
from datetime import timedelta


def game_detail(request, game_id):
    game = get_object_or_404(LiveGame, id=game_id)
    user_bets = []
    can_place_bet = True

    if request.user.is_authenticated:
        account = Acc.objects.get(user=request.user)
        user_bets = UserGame.objects.filter(user=account, game=game)

    # Check if the game is completed or the betting time has ended
    if game.status == 'completed' or (game.start_time + timedelta(minutes=5)) < timezone.now():
        can_place_bet = False

    if request.method == 'POST' and can_place_bet:
        form = BetForm(request.POST)
        if form.is_valid():
            color = form.cleaned_data['color']
            user_bet = UserGame.objects.create(
                user=account,
                game=game,
                chosen_color=color,
            )
            user_bet.save()
            return HttpResponseRedirect(reverse('game_detail', args=[game_id]))
    else:
        form = BetForm()

    return render(request, 'game/game_detail.html', {'game': game, 'form': form, 'user_bets': user_bets, 'can_place_bet': can_place_bet})
