from django.contrib import admin
from .models import GameProfile


@admin.register(GameProfile)
class GameProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'bet_amount', 'win_reward',
                    'is_active', 'created_at', 'updated_at')
    search_fields = ('name',)
    readonly_fields = ('created_at', 'updated_at')

    filter_horizontal = ()
    list_filter = ('is_active',)
