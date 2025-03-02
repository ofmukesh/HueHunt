from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import ImageSetting


@admin.register(ImageSetting)
class ImageSettingAdmin(admin.ModelAdmin):
    list_display = ('id', 'image_tag', 'updated_at')
    readonly_fields = ('image_tag',)

    def image_tag(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" width="100" height="100" />')
    image_tag.short_description = 'Image'

    def has_delete_permission(self, request, obj=None):
        return False