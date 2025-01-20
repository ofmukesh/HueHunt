from django.urls import path
from .views import PaymentView
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('', login_required(PaymentView.as_view()), name='payment'),
]
