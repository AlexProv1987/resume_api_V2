from .models import Plan
def get_user_plan(user):
    if hasattr(user, 'subscription') and user.subscription and user.subscription.plan:
        return user.subscription.plan
    return Plan.objects.get(name='Free')