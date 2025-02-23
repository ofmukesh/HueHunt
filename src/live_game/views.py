from .forms import BetForm
from .models import LiveGame
from datetime import timedelta
from django.urls import reverse
from django.utils import timezone
from user_game.models import UserGame
from account.models import Account as Acc
from utils.constants import GAME_RUN_TIME, COLOR_CHOICES
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from game_profile.models import GameProfile


def game_detail(request, game_id):
    game = get_object_or_404(LiveGame, id=game_id)
    user_bets = []
    can_place_bet = True

    if request.user.is_authenticated:
        account = Acc.objects.get(user=request.user)
        user_bets = UserGame.objects.filter(user=account, game=game)

    # Check if the game is completed or the betting time has ended
    if game.status == 'completed' or (game.start_time + timedelta(minutes=GAME_RUN_TIME)) < timezone.now():
        can_place_bet = False

    if request.method == 'POST' and can_place_bet:
        form = BetForm(request.POST)
        if form.is_valid():
            if account.balance < game.game_profile.bet_amount:
                messages.error(request, 'Insufficient balance')
            else:
                color = form.cleaned_data['color']
                user_bet = UserGame.objects.create(
                    user=account,
                    game=game,
                    chosen_color=color,
                )
                account.matches_played += 1
                account.balance -= game.game_profile.bet_amount
                account.save()
                user_bet.save()
                return HttpResponseRedirect(reverse('game_detail', args=[game_id]))
    else:
        form = BetForm()

    return render(request, 'game/game_detail.html', {
        'game': game,
        'form': form,
        'user_bets': user_bets,
        'can_place_bet': can_place_bet,
        'game_run_time': GAME_RUN_TIME,
        'color_choices': COLOR_CHOICES
    })


def create_new_games():
    # get allactive games profile from game_profile
    games = GameProfile.objects.filter(is_active=True)

    # iterate through all the games
    for game in games:
        # create a new live game for each game profile
        live_game = LiveGame.objects.create(
            game_profile=game,
            start_time=timezone.now(),
            status='ongoing',
            bet_amount=game.bet_amount
        )
        live_game.save()


def complete_live_games():
    # get all current ongoing live games
    games = LiveGame.objects.filter(status='ongoing')

    # iterate through all the games
    for game in games:
        # check if the game has ended
        if game.start_time + timedelta(minutes=GAME_RUN_TIME) < timezone.now():
            # get all the user bets for the game
            user_bets = UserGame.objects.filter(game=game)
            # get the placed color bet countings
            color_count = {}
            for color in COLOR_CHOICES:
                color_count[color[0]] = 0
            for user_bet in user_bets:
                color_count[user_bet.chosen_color] += 1

            # get the color with the lowest bet count
            lowest_bet_color = min(color_count, key=color_count.get)

            # set the lowest bet color as the winning color
            game.result = lowest_bet_color

            # now add the winning amount to the user account
            for user_bet in user_bets:
                if user_bet.chosen_color == lowest_bet_color:
                    user_bet.user.balance += game.game_profile.win_reward
                    user_bet.user.matches_won+=1
                    user_bet.user.save()

            # update the game status
            game.status = 'completed'
            game.save()
