# Generated by Django 2.0.13 on 2019-03-13 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0004_auto_20190313_0434'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storypage',
            name='date_published',
            field=models.DateField(verbose_name='Date article published'),
        ),
    ]
