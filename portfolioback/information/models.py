from django.db import models

class Skill(models.Model):
    title = models.CharField('Title', max_length=255, unique=True)
    icon = models.TextField('Icon path tag', help_text='path tag of svg icon')
    content = models.TextField('Content')
    addition = models.TextField('Additional Content')

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'


class Info(models.Model):
    image = models.ImageField(
        'Avatar',
        upload_to='images/'
    )
    age = models.PositiveSmallIntegerField('Age')
    location = models.CharField('Location', max_length=60, help_text='Specify only city, thus way it looks better')
