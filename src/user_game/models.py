import uuid
from django.db import models
from account.models import Account
from live_game.models import LiveGame
from utils.constants import COLOR_CHOICES


class UserGameManager(models.Manager):
    def get_completed_games(self, acc):
        return self.filter(user=acc, game__status='completed').order_by('-created_at')


class UserGame(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    game = models.ForeignKey(LiveGame, on_delete=models.CASCADE)
    chosen_color = models.CharField(max_length=4, choices=COLOR_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    objects = UserGameManager()

    def __str__(self):
        return f"{self.user.user.username} - {self.game} - {self.chosen_color}"
