from django.db import models
from account.models import Account
from django.core.exceptions import ValidationError


class Payment(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    upi_id = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected')
    ], default='pending')

    def __str__(self):
        return f"{self.account.user.username} - {self.amount} - {self.status}"

    def clean(self):
        if self.pk is None:  # New payment
            if self.amount > self.account.balance:
                raise ValidationError(
                    "Requested amount exceeds account balance")
        else:  # Existing payment
            old_payment = Payment.objects.get(pk=self.pk)
            if old_payment.status == 'approved':
                raise ValidationError("Approved payments cannot be edited")
            if self.status == 'approved' and old_payment.status != 'approved':
                if self.amount > self.account.balance:
                    raise ValidationError(
                        "Requested amount exceeds account balance")

    def save(self, *args, **kwargs):
        if self.pk is not None and self.status == 'approved':
            old_payment = Payment.objects.get(pk=self.pk)
            if old_payment.status != 'approved':
                self.account.balance -= self.amount
                self.account.save()
        super().save(*args, **kwargs)
