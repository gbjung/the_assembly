from __future__ import unicode_literals

from django.db import models

from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel, get_all_child_relations

from wagtail.admin.edit_handlers import (
    FieldPanel,
    FieldRowPanel,
    InlinePanel,
    MultiFieldPanel,
    PageChooserPanel,
    StreamFieldPanel,
)
from wagtail.core.fields import RichTextField, StreamField
from wagtail.core.models import Collection, Page
from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.search import index
from wagtail.snippets.models import register_snippet

from .blocks import BaseStreamBlock

@register_snippet
class Author(index.Indexed, ClusterableModel):
    """
    A Django model to store Author objects. Authors are associated with each
    story. Each Author has their own author page.

    """
    first_name = models.CharField("First name", max_length=254)
    last_name = models.CharField("Last name", max_length=254)
    title = models.CharField("Title", null=True, blank=True, max_length=254)
    introduction = models.CharField("Author Introduction", null=True, blank=True, max_length=254)
    instagram_link = models.CharField("Instagram Handle", null=True, blank=True, max_length=254)
    twitter_link = models.CharField("Twitter Handle", null=True, blank=True, max_length=254)
    facebook_link = models.CharField("Facebook Handle", null=True, blank=True, max_length=254)
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    panels = [
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('first_name', classname="col6"),
                FieldPanel('last_name', classname="col6"),
            ])
        ], "Name"),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('instagram_link', classname="col4"),
                FieldPanel('twitter_link', classname="col4"),
                FieldPanel('facebook_link', classname="col4"),
            ])
        ], "Social Media Handles"),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('title', classname="col12"),
                FieldPanel('introduction', classname="col12")
            ])
        ], "Author information"),
        ImageChooserPanel('image')
    ]

    search_fields = [
        index.SearchField('first_name'),
        index.SearchField('last_name'),
    ]

    @property
    def thumb_image(self):
        # Returns an empty string if there is no profile pic or the rendition
        # file can't be found.
        try:
            return self.image.get_rendition('fill-50x50').img_tag()
        except:
            return ''

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)

    @property
    def stories(self):
        return [n.story for n in self.author_story_relationship.all()]

    @property
    def story_count(self):
        return self.author_story_relationship.count()

    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'


class StoryCategory(models.Model):
    """
    Top level categories to classify where the stories fall under.
    IE: Culture, News, Politics, etc.
    """
    name = models.CharField(max_length=255)
    icon = models.ForeignKey(
        'wagtailimages.Image', null=True, blank=True,
        on_delete=models.SET_NULL, related_name='+'
    )

    panels = [
        FieldPanel('name'),
        ImageChooserPanel('icon'),
    ]

    def __str__(self):
        return self.name

    @property
    def thumb_image(self):
        # Returns an empty string if there is no profile pic or the rendition
        # file can't be found.
        try:
            return self.icon.get_rendition('fill-50x50').img_tag()
        except:
            return ''

    def child_stories(self):
        return self.stories.count()

    class Meta:
        verbose_name_plural = 'Story categories'
