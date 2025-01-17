from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView


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
