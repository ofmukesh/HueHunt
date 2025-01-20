from django.db import models
from account.models import Account
from utils.constants import PAYMENT_STATUS_CHOICES
from django.core.exceptions import ValidationError


class PaymentManager(models.Manager):
    # Get the payment history by account
    def get_history_by_account(self, account):
        # sorted by created_at in descending order
        return self.filter(account=account).order_by('-created_at')


class Payment(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    amount = models.IntegerField()
    upi_id = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=20, choices=PAYMENT_STATUS_CHOICES, default='pending')

    # Payment manager
    objects = PaymentManager()

    def clean(self):
        if self.amount > self.account.balance:
            raise ValidationError('Amount exceeds current balance.')

    def save(self, *args, **kwargs):
        if not self.pk:  # Only subtract balance if the payment is new
            self.clean()
            self.account.balance -= self.amount
            self.account.save()
        else:
            # Handle status changes
            old_payment = Payment.objects.get(pk=self.pk)
            if old_payment.status != self.status:
                if self.status == 'rejected' and old_payment.status == 'pending':
                    self.account.balance += self.amount
                    self.account.save()
                elif old_payment.status in ['approved', 'rejected']:
                    raise ValidationError(
                        'Cannot modify an approved or rejected payment.')

        super(Payment, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        if self.status in ['approved', 'rejected']:
            raise ValidationError(
                'Cannot delete an approved or rejected payment.')
        super(Payment, self).delete(*args, **kwargs)

    def __str__(self):
        return f"{self.account.user.username} - {self.amount} - {self.status}"
