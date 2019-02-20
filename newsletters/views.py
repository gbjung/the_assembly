from django.core.mail import get_connection, EmailMultiAlternatives
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

def send_mass_html_mail(datatuple):
    """
    Given a datatuple of (subject, text_content, html_content, from_email,
    recipient_list), sends each message to each recipient list. Returns the
    number of emails sent.

    If from_email is None, the DEFAULT_FROM_EMAIL setting is used.
    If auth_user and auth_password are set, they're used to log in.
    If auth_user is None, the EMAIL_HOST_USER setting is used.
    If auth_password is None, the EMAIL_HOST_PASSWORD setting is used.

    """
    connection = get_connection()
    messages = []
    for subject, text, html, from_email, recipient in datatuple:
        message = EmailMultiAlternatives(subject, text, from_email, recipient)
        message.attach_alternative(html, 'text/html')
        messages.append(message)

    return connection.send_messages(messages)

def send_newsletters(sender, **kwargs):
    """
    When a newsletter is published, trigger an email send
    to all Subscribers.
    """
    connection = get_connection()
    msg_html = render_to_string('newsletters/newsletter.html',
                                {'newsletter_html': kwargs['instance'].html})

    active_subscribers = Subscriber.objects.filter(is_active=True)
    emails = []
    subject = kwargs['instance'].subject
    text = None
    from_email = 'newsletter@theassembly.xyz'

    for subscriber in active_subscribers.iterator():
        email = EmailMultiAlternatives(subject, text, from_email, [subscriber.email])
        email.attach_alternative(msg_html, 'text/html')
        emails.append(email)

    return connection.send_messages(emails)


page_published.connect(send_newsletters, sender=Newsletter)
