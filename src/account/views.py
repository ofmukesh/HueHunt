from django.shortcuts import render


def account_view(request):
    return render(request, 'account/account.html')
