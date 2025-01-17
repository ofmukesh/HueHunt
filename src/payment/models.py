from django.db import models
from account.models import Account
from django.core.exceptions import ValidationError
from utils.constants import PAYMENT_STATUS_CHOICES


class Payment(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    amount = models.IntegerField()
    upi_id = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=20, choices=PAYMENT_STATUS_CHOICES, default='pending')

    def __str__(self):
        return f"{self.account.user.username} - {self.amount} - {self.status}"