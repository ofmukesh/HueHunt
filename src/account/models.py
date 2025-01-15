import uuid
from django.db import models
from django.contrib.auth.models import User


# Account manager is used to create custom queries for the Account model
class AccountManager(models.Manager):
    # Get account by user
    def get_by_user(self, user):
        return self.get(user=user)

    # Get account by id
    def get_by_id(self, acc_id):
        return self.get(pk=acc_id)


# Account model is used to store user account details
class Account(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.IntegerField(default=0)
    matches_played = models.IntegerField(default=0)
    matches_won = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = AccountManager()  # Custom manager

    def __str__(self):
        return self.user.username
