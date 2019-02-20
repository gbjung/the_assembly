from django.db import models

from wagtail.core.models import Page
from wagtail.admin.edit_handlers import PageChooserPanel
from stories.views import get_recent_stories

class HomePage(Page):
    parent_page_types = ['wagtailcore.Page']
    featured_story = models.ForeignKey('stories.StoryPage', on_delete=models.SET_NULL, null=True, blank=True)
    content_panels = Page.content_panels + [
        PageChooserPanel('featured_story'),
    ]

    def get_context(self, request):
        context = super().get_context(request)

        # Add extra variables and return the updated context
        if self.featured_story:
            context['featured_story'] = self.featured_story
            context['recent_stories'] = get_recent_stories(self.featured_story.id, 0)

        return context

    @classmethod
    def can_create_at(cls, parent):
        # You can only create one of these!
        return super(HomePage, cls).can_create_at(parent) \
            and not cls.objects.exists()
