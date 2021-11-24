from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.utils import timezone


class Transfer(models.Model):
    sender = models.ForeignKey(User, null=False, editable=False, on_delete=models.PROTECT)
    recipient_name = models.CharField(null=False, blank=False, max_length=80)
    recipient_account = models.CharField(null=False, max_length=26)
    title = models.CharField(null=False, blank=False, max_length=120)
    amount = models.DecimalField(null=False, decimal_places=2, max_digits=10)
    date = models.DateTimeField(default=timezone.now)
