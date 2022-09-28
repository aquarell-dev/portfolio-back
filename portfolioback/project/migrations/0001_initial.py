# Generated by Django 4.1.1 on 2022-09-21 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StackItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80, verbose_name='Title')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Title')),
                ('image', models.ImageField(upload_to='images/', verbose_name='Image')),
                ('budget', models.PositiveIntegerField(verbose_name='Budget')),
                ('short_description', models.TextField(blank=True, max_length=80, null=True, verbose_name='Short Description')),
                ('description', models.TextField(verbose_name='Description')),
                ('stack', models.ManyToManyField(to='project.stackitem', verbose_name='Stack')),
            ],
            options={
                'verbose_name': 'Project',
                'verbose_name_plural': 'Projects',
            },
        ),
    ]