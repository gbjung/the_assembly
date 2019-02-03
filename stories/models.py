from __future__ import unicode_literals

from django import forms
from django.db import models

from modelcluster.contrib.taggit import ClusterTaggableManager
from modelcluster.fields import ParentalKey, ParentalManyToManyField

from taggit.models import TaggedItemBase

from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, StreamFieldPanel
from wagtail.core.fields import StreamField
from wagtail.core.models import Page, Orderable
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.search import index
from wagtail.snippets.edit_handlers import SnippetChooserPanel

from base.blocks import BaseStreamBlock

# Create your models here.
#
class StoryPageTag(TaggedItemBase):
    """
    This model allows us to create a many-to-many relationship between
    the StoryPage object and tags.
    http://docs.wagtail.io/en/latest/reference/pages/model_recipes.html#tagging
    """
    content_object = ParentalKey('StoryPage', related_name='tagged_items', on_delete=models.CASCADE)


class StoryAuthorRelationship(Orderable, models.Model):
    """
    This defines the two way relationship between Authors and Stories
    """
    story = ParentalKey(
        'StoryPage', related_name='story_author_relationship', on_delete=models.CASCADE
    )
    authors = models.ForeignKey(
        'authors.Author', related_name='author_story_relationship', on_delete=models.CASCADE
    )
    panels = [
        SnippetChooserPanel('authors')
    ]

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

class StoryPage(Page):
    """
    A Story Page. Stories are linked with an Author and a category.
    """
    introduction = models.TextField(
        help_text='Text to describe the page',
        blank=True)
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='Landscape mode only; horizontal width between 1000px and 3000px.'
    )
    body = StreamField(
        BaseStreamBlock(), verbose_name="Page body", blank=False
    )
    subtitle = models.CharField(blank=True, max_length=255)
    tags = ClusterTaggableManager(through=StoryPageTag, blank=True)
    categories = ParentalManyToManyField('StoryCategory',  related_name='stories', blank=True)
    date_published = models.DateField(
        "Date article published", blank=True, null=True
        )

    content_panels = Page.content_panels + [
        FieldPanel('subtitle', classname="full"),
        FieldPanel('introduction', classname="full"),
        ImageChooserPanel('image'),
        StreamFieldPanel('body'),
        FieldPanel('date_published'),
        InlinePanel(
            'story_author_relationship', label="Author(s)",
            panels=None, min_num=1),
        FieldPanel('categories', widget=forms.CheckboxSelectMultiple),
        FieldPanel('tags'),
    ]

    search_fields = Page.search_fields + [
        index.SearchField('body'),
    ]

    def authors(self):
        """
        Returns the Story's related Authors.
        """
        authors = [
            n.author for n in self.story_author_relationship.all()
        ]

        return authors

    @property
    def get_tags(self):
        """
        Similar to the authors function above we're returning all the tags that
        are related to the blog post into a list we can access on the template.
        We're additionally adding a URL to access BlogPage objects with that tag
        """
        tags = self.tags.all()
        for tag in tags:
            tag.url = '/'+'/'.join(s.strip('/') for s in [
                self.get_parent().url,
                'tags',
                tag.slug
            ])
        return tags

    # Specifies parent to BlogPage as being BlogIndexPages
    # parent_page_types = ['BlogIndexPage']

    # Specifies what content types can exist as children of BlogPage.
    # Empty list means that no child content types are allowed.
    subpage_types = []
