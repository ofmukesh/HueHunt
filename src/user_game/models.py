import uuid
from django.db import models
from account.models import Account
from live_game.models import LiveGame

COLOR_CHOICES = [
    ('red', 'Red'),
    ('blue', 'Blue'),
]


class UserGame(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    game = models.ForeignKey(LiveGame, on_delete=models.CASCADE)
    chosen_color = models.CharField(max_length=4, choices=COLOR_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.user.username} - {self.game} - {self.chosen_color}"

    def save(self, *args, **kwargs):
        if not self.pk:  # Check if this is a new instance
            self.user.matches_played += 1
            self.user.save()
        super().save(*args, **kwargs)
