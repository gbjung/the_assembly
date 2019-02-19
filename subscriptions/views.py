import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
from subscriptions.models import Subscriber

@csrf_protect
def create_new_subscriber(request):
    if request.method == "POST":
        email = request.POST.get('email')
        subscriber, created = Subscriber.objects.get_or_create(email=email)
        response = {}

        if created:
            response["msg"] = True
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
