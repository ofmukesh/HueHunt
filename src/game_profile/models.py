from django.db import models


class GameProfile(models.Model):
    name = models.CharField(max_length=255)
    bet_amount = models.DecimalField(max_digits=10, decimal_places=2)
    win_reward = models.DecimalField(max_digits=10, decimal_places=2)
    loss_return = models.DecimalField(max_digits=10, decimal_places=2)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
