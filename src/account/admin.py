from django.contrib import admin
from .models import Account


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'balance', 'matches_played',
                    'matches_won', 'is_active', 'created_at', 'updated_at')
    search_fields = ('uuid', 'user__username')
    readonly_fields = ('created_at', 'updated_at',
                       'matches_played', 'matches_won', 'id')

    filter_horizontal = ()
    list_filter = ('is_active', 'created_at', 'updated_at')
