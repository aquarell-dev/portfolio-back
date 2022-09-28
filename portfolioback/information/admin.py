from django.contrib import admin

from .models import Skill, Info

from utils.mixins import SvgPreviewMixin, ImagePreviewMixin

@admin.register(Skill)
class AboutAdmin(SvgPreviewMixin, admin.ModelAdmin):
    list_display = [field.name for field in Skill._meta.get_fields() if field.name not in ['icon']] + ['preview_svg']
    list_display_links = ['id']


@admin.register(Info)
class InfoAdmin(ImagePreviewMixin, admin.ModelAdmin):
    description = 'Avatar'

    list_display = [field.name for field in Info._meta.get_fields() if field.name not in ['image']] + ['preview_image']
    list_display_links = ['id']
