import json
from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
from mailchimp3 import MailChimp

from subscriptions.models import Subscriber

@csrf_protect
def create_new_subscriber(request):
    if request.method == "POST":
        email = request.POST.get('email')
        subscriber, created = Subscriber.objects.get_or_create(email=email)
        response = {}

        if created:
            response["msg"] = True
            create_mailchimp_subscriber(email)
        else:
            response["msg"] = False

        return HttpResponse(
            json.dumps(response),
            content_type="application/json"
            )

    return HttpResponse(
        json.dumps({"msg": "bad"}),
        content_type="application/json"
        )


def create_mailchimp_subscriber(email):
    client = MailChimp(mc_api=settings.MAILCHIMP_KEY, mc_user=settings.MAILCHIMP_USER)
    try:
        client.lists.members.create(settings.MAILCHIMP_LIST_ID,
                                    data={'email_address': email, 'status': 'subscribed'})
    except:
        print("If I was actually logging anything, I'd log a bad email here LOL")
