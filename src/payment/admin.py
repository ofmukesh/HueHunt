from django.contrib import admin
from .models import Payment, AddMoneyRequest


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('account', 'amount', 'status', 'created_at')
    search_fields = ('account__user__username', 'status')
    list_filter = ('status', 'created_at')
    readonly_fields = ('created_at', 'amount', 'upi_id', 'account')

    def get_readonly_fields(self, request, obj=None):
        if obj and (obj.status == 'approved' or obj.status == 'rejected'):
            return self.readonly_fields + ('status',)
        return self.readonly_fields


@admin.register(AddMoneyRequest)
class AddMoneyRequestAdmin(admin.ModelAdmin):
    list_display = ['account', 'amount', 'transaction_id', 'name', 'status', 'created_at']
    list_filter = ['status', 'created_at']
    search_fields = ['account__user__username', 'transaction_id', 'name']
    readonly_fields = ['created_at']
    list_per_page = 20
    
    def save_model(self, request, obj, form, change):
        if change and 'status' in form.changed_data:
            if obj.status == 'approved':
                obj.account.balance += obj.amount
                obj.account.save()
            elif obj.status == 'rejected' and form.initial['status'] == 'approved':
                obj.account.balance -= obj.amount
                obj.account.save()
            elif obj.status == 'pending' and form.initial['status'] == 'approved':
                obj.account.balance -= obj.amount
                obj.account.save()
        super().save_model(request, obj, form, change)