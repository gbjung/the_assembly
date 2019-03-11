# Generated by Django 2.0.13 on 2019-03-03 20:48

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0040_page_draft_title'),
        ('wagtailimages', '0020_add-verbose-name'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('left_title', models.TextField(blank=True)),
                ('left_text', wagtail.core.fields.RichTextField()),
                ('right_title', models.TextField(blank=True)),
                ('right_text', wagtail.core.fields.RichTextField()),
                ('bio_title', models.TextField(blank=True)),
                ('amina_text', wagtail.core.fields.RichTextField()),
                ('amina_instagram', models.CharField(blank=True, max_length=254, null=True, verbose_name="Amina's Instagram Handle")),
                ('amina_twitter', models.CharField(blank=True, max_length=254, null=True, verbose_name="Amina's Twitter Handle")),
                ('lincoln_text', wagtail.core.fields.RichTextField()),
                ('lincoln_instagram', models.CharField(blank=True, max_length=254, null=True, verbose_name="Lincoln's Instagram Handle")),
                ('lincoln_twitter', models.CharField(blank=True, max_length=254, null=True, verbose_name="Lincoln's Twitter Handle")),
                ('bio_image', models.ForeignKey(blank=True, help_text='Landscape mode only; horizontal width between 1000px and 3000px.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]