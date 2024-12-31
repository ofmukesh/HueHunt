from django.contrib import admin
from .models import LiveGame


@admin.register(LiveGame)
class LiveGameAdmin(admin.ModelAdmin):
    list_display = ('game_profile', 'start_time', 'end_time',
                    'status', 'result', 'bet_amount', 'created_at')
    list_filter = ('status', 'result')
    search_fields = ('game_profile__name',)
    readonly_fields = ('bet_amount', 'end_time', 'status',
                       'result')  # Make fields read-only

    def save_model(self, request, obj, form, change):
        obj.bet_amount = obj.game_profile.bet_amount
        super().save_model(request, obj, form, change)

    def get_readonly_fields(self, request, obj=None):
        if obj and obj.status == 'completed':
            return self.readonly_fields + ('game_profile', 'start_time', 'created_at')
        return self.readonly_fields
