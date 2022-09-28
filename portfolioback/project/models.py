from django.db import models

class StackItem(models.Model):
    title = models.CharField('Title', max_length=80)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Stack Item'
        verbose_name_plural = 'Stack Items'

class Project(models.Model):
    title = models.CharField('Title', max_length=200)
    image = models.ImageField('Image', upload_to='images/')
    budget = models.DecimalField('Budget', max_digits=6, decimal_places=2, help_text='In US dollars')
    short_description = models.TextField('Short Description', max_length=80, blank=True, null=True)
    description = models.TextField('Description')
    stack = models.ManyToManyField(StackItem, verbose_name='Stack')
    github = models.URLField('Github Link')
    temp_link = models.URLField('Temporary project link', help_text='Some test hosting like vercel, etc...', blank=True, null=True)
    actual_link = models.URLField('Project Link', blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.short_description:
            self.short_description = self.description[0:80] + '...'
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'
