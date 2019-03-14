# Generated by Django 2.0.13 on 2019-03-12 03:44

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('wagtailredirects', '0006_redirect_increase_max_length'),
        ('wagtailcore', '0041_group_collection_permissions_verbose_name_plural'),
        ('contenttypes', '0002_remove_content_type_name'),
        ('wagtailimages', '0001_squashed_0021'),
        ('wagtailforms', '0003_capitalizeverbose'),
        ('stories', '0002_auto_20190303_2146'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='StoryCategory',
            new_name='Issue',
        ),
        migrations.AlterModelOptions(
            name='issue',
            options={'verbose_name_plural': 'Issues'},
        ),
    ]