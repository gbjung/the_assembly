from django.conf.urls import url
from subscriptions.views import create_new_subscriber

urlpatterns = [
    url(r'^new/?', create_new_subscriber),
]
