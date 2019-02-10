# Generated by Django 2.1.5 on 2019-02-03 03:46

from django.db import migrations, models
import django.db.models.deletion
import wagtail.search.index


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailimages', '0001_squashed_0021'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=254, verbose_name='First name')),
                ('last_name', models.CharField(max_length=254, verbose_name='Last name')),
                ('title', models.CharField(blank=True, max_length=254, null=True, verbose_name='Title')),
                ('introduction', models.CharField(blank=True, max_length=254, null=True, verbose_name='Author Introduction')),
                ('instagram_link', models.CharField(blank=True, max_length=254, null=True, verbose_name='Instagram Handle')),
                ('twitter_link', models.CharField(blank=True, max_length=254, null=True, verbose_name='Twitter Handle')),
                ('facebook_link', models.CharField(blank=True, max_length=254, null=True, verbose_name='Facebook Handle')),
                ('image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
            ],
            options={
                'verbose_name': 'Author',
                'verbose_name_plural': 'Authors',
            },
            bases=(wagtail.search.index.Indexed, models.Model),
        ),
    ]