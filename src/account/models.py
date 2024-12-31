import uuid
from django.db import models
from django.contrib.auth.models import User


class Account(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.DecimalField(
        max_digits=10, decimal_places=2, default=0.00)
    matches_played = models.IntegerField(default=0)
    matches_won = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username
