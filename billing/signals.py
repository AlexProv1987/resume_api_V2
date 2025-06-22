from django.dispatch import receiver
from django.db.models.signals import post_save
from user.models import User
""" 
    if this ever actually becomes used well move over the sub info per applicant to cache
    Invalidate on delete or save
    on Save reset cache key
"""
@receiver(post_save, sender=User)
def create_subscription_if_needed(sender, instance, created, **kwargs):
    if created and not hasattr(instance, 'subscription'):
        from plans.models import Plan
        from billing.models import Subscription

        free_plan = Plan.objects.filter(name="Free").first()
        if not free_plan:
            free_plan = Plan.objects.create(name="Free", description="Default free tier", is_active=True)

        Subscription.objects.create(user=instance, plan=free_plan)