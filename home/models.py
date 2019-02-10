from django.db import models

from wagtail.core.models import Page
from wagtail.admin.edit_handlers import PageChooserPanel

class HomePage(Page):
    parent_page_types = ['wagtailcore.Page']
    featured_story = models.ForeignKey('stories.StoryPage', on_delete=models.SET_NULL, null=True, blank=True)
    content_panels = Page.content_panels + [
        PageChooserPanel('featured_story'),
    ]

    @classmethod
    def can_create_at(cls, parent):
        # You can only create one of these!
        return super(HomePage, cls).can_create_at(parent) \
            and not cls.objects.exists()
