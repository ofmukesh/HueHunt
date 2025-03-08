from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from .forms import RegistrationForm
from .models import Account


# Account view
class AccountView(View):
    """
    View to display the account page.
    """

    def get(self, request):
        return render(request, 'account/account.html')


# Custom login view
class CustomLoginView(LoginView):
    """
    Custom login view that redirects authenticated users to the home page.
    """

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/')
        return super().dispatch(request, *args, **kwargs)


# Forgot password view
def forgot_password(request):
    """
    View to render the forgot password page.
    """
    return render(request, 'account/forgot_password.html')


# Register view
class RegisterView(View):
    def get(self, request):
        form = RegistrationForm()
        return render(request, 'registration/register.html', {'form': form})

    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Account.objects.create(user=user, balance=0)
            login(request, user)
            return redirect('/')
        return render(request, 'registration/register.html', {'form': form})
