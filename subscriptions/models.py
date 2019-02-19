from django.utils import timezone
from django.db import models

class Subscriber(models.Model):
    '''
    Model for saving subscribers for the Assembly.
    Newsletters/emails will be sent to subscribers.
    '''

    email = models.EmailField(unique=True, error_messages={'unique':'Already a Subscriber'})
    join_date = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)


    def __str__(self):
        return "@{}".format(self.email)
