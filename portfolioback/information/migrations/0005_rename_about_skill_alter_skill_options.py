# Generated by Django 4.1.1 on 2022-09-21 11:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('information', '0004_rename_avatar_info_image'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='About',
            new_name='Skill',
        ),
        migrations.AlterModelOptions(
            name='skill',
            options={'verbose_name': 'Skill', 'verbose_name_plural': 'Skills'},
        ),
    ]
