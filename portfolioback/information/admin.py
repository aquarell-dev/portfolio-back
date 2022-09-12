from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Info


class SvgPreviewMixin:
    def preview_svg(self, obj):
        if obj:
            return mark_safe('<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" '
                             'stroke-width="1.5" stroke="currentColor" width="50">'
                             f'{obj.icon}'
                             '</svg>')


@admin.register(Info)
class InfoAdmin(SvgPreviewMixin, admin.ModelAdmin):
    list_display = [field.name for field in Info._meta.get_fields() if field.name not in ['icon']] + ['preview_svg']
    list_display_links = ['id']
