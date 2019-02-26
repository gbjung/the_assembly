from django.db import models
from django.utils import timezone
from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel

class NewsletterIndexPage(Page):
    content_panels = Page.content_panels
    parent_page_types = ['home.HomePage']
    subpage_types = ['newsletters.Newsletter']

    @classmethod
    def can_create_at(cls, parent):
        # You can only create one of these!
        return super(NewsletterIndexPage, cls).can_create_at(parent) \
            and not cls.objects.exists()

class Newsletter(Page):
    date = models.DateTimeField(default=timezone.now)
    html = models.TextField(blank=False)
    subject = models.TextField(blank=False)

    parent_page_types = ['newsletters.NewsletterIndexPage']
    subpage_types = []
    promote_panels = [FieldPanel('slug')]

    content_panels = Page.content_panels + [
        FieldPanel('subject'),
        FieldPanel('date'),
        FieldPanel('html'),
    ]

    def sent(self):
        if self.first_published_at:
            return True
        return False


    def get_context(self, request):
        context = super(Newsletter, self).get_context(request)
        context['newsletter_html'] = self.html

        return context
