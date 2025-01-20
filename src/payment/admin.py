from django.contrib import admin
from .models import Payment


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
