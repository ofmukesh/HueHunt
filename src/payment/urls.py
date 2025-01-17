from django.urls import path
from .views import payment_view
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('', login_required(payment_view), name='payment'),
]
