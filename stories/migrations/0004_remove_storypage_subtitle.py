# Generated by Django 2.1.5 on 2019-02-19 03:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0003_auto_20190203_0702'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='storypage',
            name='subtitle',
        ),
    ]