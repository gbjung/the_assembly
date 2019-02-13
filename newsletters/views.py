from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.views.generic.base import TemplateView
from wagtail.core.signals import page_published
from newsletters.models import Newsletter
from subscriptions.models import Subscriber


class NewsletterMakerView(TemplateView):

    template_name = "newsletter_maker.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

def send_newsletters(sender, **kwargs):
    """
    When a newsletter is published, trigger an email send
    to all Subscribers.
    """
    msg_html = render_to_string('newsletters/newsletter.html',
                                {'newsletter_html': kwargs['instance'].html})
                                
    active_subscribers = Subscriber.objects.filter(active=True)
    for subscriber in active_subscribers.iterator():
        send_mail(
            kwargs['instance'].subject,
            'Here is the message.',
            'gyeongbae.jj',
            ['gyeongbae.jj@gmail.com'],
            fail_silently=False,
            html_message=msg_html,
        )
    return

page_published.connect(send_newsletters, sender=Newsletter)
