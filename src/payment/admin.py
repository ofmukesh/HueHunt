from django.contrib import admin
from .models import Payment


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('account', 'amount', 'status', 'created_at')
    search_fields = ('account__user__username', 'status')
    list_filter = ('status', 'created_at')
    readonly_fields = ('created_at',)