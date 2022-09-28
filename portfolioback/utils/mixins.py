from django.utils.safestring import mark_safe


class SvgPreviewMixin:
    def preview_svg(self, obj):
        if obj:
            return mark_safe('<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" '
                             'stroke-width="1.5" stroke="currentColor" width="50">'
                             f'{obj.icon}'
                             '</svg>')


class ImagePreviewMixin:
    def preview_image(self, obj):
        if obj:
            return mark_safe(f'<img src="{obj.image.url}" width=50>')
