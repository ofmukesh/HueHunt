from django.contrib import admin
from .models import Account


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    # fields list to display on admin panel
    list_display = ('id', 'user', 'balance', 'matches_played',
                    'matches_won', 'is_active', 'created_at', 'updated_at')

    # fields that is not editable by super-admin
    readonly_fields = ('created_at', 'updated_at',
                       'matches_played', 'matches_won', 'id')

    # search & filter fields
    search_fields = ('uuid', 'user__username')
    list_filter = ('is_active', 'created_at', 'updated_at')
