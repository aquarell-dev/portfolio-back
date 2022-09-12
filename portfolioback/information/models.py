from django.db import models

class Info(models.Model):
    title = models.CharField('Title', max_length=255, unique=True)
    icon = models.TextField('Icon path tag', help_text='path tag of svg icon')
    content = models.TextField('Content')
    addition = models.TextField('Additional Content')

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'About'
        verbose_name_plural = 'Abouts'
