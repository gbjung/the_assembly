from django.db import models
from wagtail.admin.edit_handlers import (
    FieldPanel,
    FieldRowPanel,
    MultiFieldPanel
)
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import BaseChooserPanel



class AboutPage(Page):
    left_title_top = models.TextField(blank=True)
    left_title_bottom = models.TextField(blank=True)
    left_text = RichTextField()
    right_title_top = models.TextField(blank=True)
    right_title_bottom = models.TextField(blank=True)
    right_text = RichTextField()
    video_url = models.URLField("Embed Url", blank=True)
    bio_title_top = models.TextField(blank=True)
    bio_title_bottom = models.TextField(blank=True)
    bio_image  = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='Landscape mode only; horizontal width between 1000px and 3000px.'
    )
    amina_text = RichTextField()
    amina_instagram = models.CharField("Amina's Instagram Handle", null=True, blank=True, max_length=254)
    amina_twitter = models.CharField("Amina's Twitter Handle", null=True, blank=True, max_length=254)

    lincoln_text = RichTextField()
    lincoln_instagram = models.CharField("Lincoln's Instagram Handle", null=True, blank=True, max_length=254)
    lincoln_twitter = models.CharField("Lincoln's Twitter Handle", null=True, blank=True, max_length=254)

    parent_page_types = ['home.HomePage']
    subpage_types = []
    promote_panels = []
    settings_panels = []
    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('left_title_top'),
            FieldPanel('left_title_bottom')
        ], "Left Title"),
        FieldPanel('left_text'),
        MultiFieldPanel([
            FieldPanel('right_title_top'),
            FieldPanel('right_title_bottom')
        ], "Right Title"),
        FieldPanel('right_text'),
        FieldPanel('video_url'),
        MultiFieldPanel([
            FieldPanel('bio_title_top'),
            FieldPanel('bio_title_bottom')
        ], "Bio Title"),
        ImageChooserPanel('bio_image'),
        FieldPanel('amina_text'),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('amina_instagram', classname="col6"),
                FieldPanel('amina_twitter', classname="col6"),
            ])
        ], "Amina's Social Media Handles"),
        FieldPanel('lincoln_text'),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('lincoln_instagram', classname="col6"),
                FieldPanel('lincoln_twitter', classname="col6"),
            ])
        ], "Lincoln's Social Media Handles"),
    ]

    @classmethod
    def can_create_at(cls, parent):
        # You can only create one of these!
        return super(AboutPage, cls).can_create_at(parent) \
            and not cls.objects.exists()
