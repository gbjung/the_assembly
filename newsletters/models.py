from django.db import models
from django.utils import timezone


class Newsletter(models.Model):
    title = models.TextField(
        help_text='Text to describe the Newsletter',
        blank=True)
    date = models.DateTimeField(default=timezone.now)
    sent = models.BooleanField(default=False)
    html = models.TextField()
