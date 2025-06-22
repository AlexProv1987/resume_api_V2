from django.shortcuts import get_object_or_404
from api.applicant.models import Applicant
from plans.utils import get_user_plan
from django.contrib.contenttypes.models import ContentType
from plans.models import RecordLimit
class EnforcePlanLimitMixin:
    """
    Mixin to limit API results based on applicant's current plan.
    Assumes an `?applicant=<pk>` is passed in query params.
    """

    applicant_param = 'applicant'  # override if using different key

    def get_queryset(self):
        queryset = super().get_queryset()

        applicant_pk = self.request.query_params.get(self.applicant_param,None)
        
        if not applicant_pk:
            return queryset.none()

        applicant = get_object_or_404(Applicant, pk=applicant_pk)
        plan = get_user_plan(applicant.user_reltn)
        
        model_cls = self.queryset.model
        content_type = ContentType.objects.get_for_model(model_cls)
        
        try:
            record_limit = RecordLimit.objects.get(plan=plan, content_type=content_type)
            limit = record_limit.max_records
        except RecordLimit.DoesNotExist:
            return queryset.none()
        
        return queryset.filter(applicant_reltn=applicant)[:limit]
