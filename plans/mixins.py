from django.core.exceptions import ValidationError
from plans.models import RecordLimit
from .utils import get_user_plan

class EnforceRecordLimitMixin:
    def get_plan(self):
        user = None

        if hasattr(self, 'applicant') and hasattr(self.applicant, 'user'):
            user = self.applicant.user_reltn

        elif hasattr(self, 'work_history') and hasattr(self.work_history, 'applicant'):
            user = self.work_history.applicant_reltn.user_reltn

        elif hasattr(self, 'project') and hasattr(self.project, 'applicant'):
            user = self.project.applicant_reltn.user_reltn

        if not user:
            raise ValidationError("Cannot resolve user from this model instance.")

        if user.is_superuser:
            return None

        return get_user_plan(user)

    def get_existing_count(self):
        model_class = self.__class__

        if hasattr(self, 'applicant'):
            return model_class.objects.filter(applicant=self.applicant).count()

        if hasattr(self, 'work_history'):
            return model_class.objects.filter(work_history=self.work_history).count()

        if hasattr(self, 'project'):
            return model_class.objects.filter(project=self.project).count()

        raise ValidationError("Cannot count related objects for this model.")

    def check_record_limit(self): 
        plan = self.get_plan()
        model_name = self.__class__.__name__
        limit = RecordLimit.objects.filter(plan=plan, model_name=model_name).first()

        if limit and self.get_existing_count() >= limit.max_records:
            raise ValidationError(f"Limit of {limit.max_records} {model_name} records reached for your plan.")

    def save(self, *args, **kwargs):
        self.check_record_limit()
        super().save(*args, **kwargs)