from django.contrib import admin
from .models import UserGame


@admin.register(UserGame)
class UserGameAdmin(admin.ModelAdmin):
    list_display = ('user', 'game', 'chosen_color',
                    'game__bet_amount', 'created_at')
    search_fields = ('user__user__username', 'chosen_color',)
    list_filter = ('chosen_color', 'created_at')
    readonly_fields = ('created_at',)
