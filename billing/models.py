from django.db import models
from django.conf import settings
from plans.models import Plan

class Subscription(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="subscription")
    plan = models.ForeignKey(Plan, on_delete=models.SET_NULL, null=True)
    monthly_fee = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)

    is_active = models.BooleanField(default=False)
    is_trial = models.BooleanField(default=True)
    trial_start = models.DateTimeField(auto_now_add=True)
    trial_end = models.DateTimeField(null=True, blank=True)

    payment_customer_id = models.CharField(max_length=255, blank=True, null=True)
    subscription_id = models.CharField(max_length=255, blank=True, null=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
