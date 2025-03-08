from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from .views import AccountView, CustomLoginView, forgot_password, RegisterView

urlpatterns = [
    path('', login_required(AccountView.as_view()), name='account'),
    path('login/',
         CustomLoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/',
         auth_views.LogoutView.as_view(next_page='/account/login/'), name='logout'),
    path('forgot-password/', forgot_password, name='forgot_password'),
    path('register/', RegisterView.as_view(), name='register'),
]
