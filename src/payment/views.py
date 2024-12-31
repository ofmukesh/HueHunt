from django.shortcuts import render


def payment_view(request):
    return render(request, 'account/payment.html')
