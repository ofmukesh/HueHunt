import uuid
from django.db import models
from game_profile.models import GameProfile
from utils.constants import COLOR_CHOICES


class LiveGameManager(models.Manager):
    def get_ongoing_games(self):
        return self.filter(status='ongoing').order_by('-created_at')


class LiveGame(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    game_profile = models.ForeignKey(GameProfile, on_delete=models.CASCADE)
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=[
        ('ongoing', 'Ongoing'),
        ('completed', 'Completed')
    ], default='ongoing')
    result = models.CharField(
        max_length=4, choices=COLOR_CHOICES, blank=True, null=True)
    bet_amount = models.DecimalField(
        max_digits=10, decimal_places=2, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)

    objects = LiveGameManager()

    def __str__(self):
        return f"{self.game_profile.name} - {self.status}"

    def save(self, *args, **kwargs):
        if not self.pk:  # Check if this is a new instance
            self.bet_amount = self.game_profile.bet_amount
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        if self.status == 'completed':
            raise ValueError("Cannot delete a completed game.")
        super().delete(*args, **kwargs)
