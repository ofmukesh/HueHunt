from django.urls import path
from .views import PaymentView, AddMoneyView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', login_required(PaymentView.as_view()), name='payment'),
    path('add/', login_required(AddMoneyView.as_view()), name='add_money'),
]
