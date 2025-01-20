from .models import Payment
from django.views import View
from .forms import PaymentForm
from account.models import Account
from django.shortcuts import render, redirect
from django.core.exceptions import ValidationError


class PaymentView(View):
    # Get method to render the payment template
    def get(self, request):
        user = request.user  # Get the logged in user
        account = Account.objects.get_by_user(
            user=user)  # Get the account of the user

        # Get the balance and withdrawals of the user
        withdrawals = Payment.objects.get_history_by_account(account)

        # Context to be passed to the template
        context = {
            'balance': account.balance,
            'withdrawals': withdrawals,
            'form': PaymentForm(balance=account.balance)
        }

        # Render the payment template
        return render(request, 'account/payment.html', context)

    def post(self, request):
        # Get the user account and balance
        user = request.user
        account = Account.objects.get_by_user(user=user)
        balance = account.balance

        # Process the form
        form = PaymentForm(request.POST, balance=balance)
        if form.is_valid():
            amount = form.cleaned_data['amount']
            upi_id = form.cleaned_data['upi_id']

            # Create a payment
            try:
                Payment.objects.create(
                    account=account, amount=amount, upi_id=upi_id)
                return redirect('payment')  # Redirect to the payment page
            except ValidationError as e:
                form.add_error(None, e.message)

        # If form is not valid, re-render the page with the form errors
        withdrawals = Payment.objects.get_history_by_account(account)
        context = {
            'balance': balance,
            'withdrawals': withdrawals,
            'form': form
        }
        return render(request, 'account/payment.html', context)
