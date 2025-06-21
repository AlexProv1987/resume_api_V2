from django.db.models.signals import post_migrate
from django.dispatch import receiver
from .models import Plan

@receiver(post_migrate)
def create_default_plan(sender, **kwargs):
    if sender.name != "plans":
        return
    Plan.objects.get_or_create(name="Free", defaults={"description": "Default free tier"})