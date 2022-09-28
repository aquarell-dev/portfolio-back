from django.contrib import admin

from .models import Project, StackItem

from utils.mixins import ImagePreviewMixin


@admin.register(StackItem)
class StackAdmin(admin.ModelAdmin):
    list_display = ['title']
    list_display_links = ['title']


@admin.register(Project)
class ProjectAdmin(ImagePreviewMixin, admin.ModelAdmin):
    list_display = [
        field.name for field in Project._meta.get_fields()
        if field.name not in ['stack', 'image']
    ] + ['preview_image']
    list_display_links = ['id']
    search_fields = ['id', 'title']

    save_on_top = True
