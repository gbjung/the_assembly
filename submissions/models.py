from django.db import models
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField

class SubmissionPage(Page):
    subtitle = models.TextField(blank=True)
    body_text = RichTextField()
    typeform_url = models.URLField(blank=False)

    parent_page_types = ['home.HomePage']
    subpage_types = []
    promote_panels = []
    settings_panels = []
    content_panels = Page.content_panels + [
        FieldPanel('subtitle'),
        FieldPanel('body_text'),
        FieldPanel('typeform_url'),
    ]

    @classmethod
    def can_create_at(cls, parent):
        # You can only create one of these!
        return super(SubmissionPage, cls).can_create_at(parent) \
            and not cls.objects.exists()
