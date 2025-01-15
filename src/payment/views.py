from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Payment
from account.models import Account


@login_required
def payment_view(request):
    user = request.user
    account = Account.objects.get(user=user)
    balance = account.balance
    withdrawals = Payment.objects.filter(
        account=account).order_by('-created_at')

    if request.method == 'POST':
        amount = request.POST.get('amount')
        if amount:
            amount = int(amount)
        if amount and 100 <= amount <= balance:
            Payment.objects.create(account=account, amount=amount)
            account.balance -= amount
            account.save()
            return redirect('payment')

    context = {
        'balance': balance,
        'withdrawals': withdrawals,
    }
    return render(request, 'account/payment.html', context)
