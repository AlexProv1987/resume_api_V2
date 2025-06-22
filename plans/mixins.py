from django.core.exceptions import ValidationError
from plans.models import RecordLimit
from .utils import get_user_plan

class EnforceRecordLimitMixin:
    
    def get_plan(self):
        user = None
        print(self)
        if hasattr(self, 'applicant_reltn') and hasattr(self.applicant_reltn, 'user_reltn'):
            user = self.applicant_reltn.user_reltn

        elif hasattr(self, 'work_reltn') and hasattr(self.work_reltn, 'applicant_reltn'):
            user = self.work_reltn.applicant_reltn.user_reltn

        elif hasattr(self, 'project_reltn') and hasattr(self.project_reltn, 'applicant_reltn'):
            user = self.project_reltn.applicant_reltn.user_reltn

        if not user:
            raise ValidationError("Cannot resolve user from this model instance.")

        if user.is_superuser:
            return None

        return get_user_plan(user)

    def get_existing_count(self):
        model_class = self.__class__

        if hasattr(self, 'applicant_reltn'):
            return model_class.objects.filter(applicant_reltn=self.applicant_reltn).count()

        if hasattr(self, 'work_reltn'):
            print(self.work_reltn.applicant_reltn)
            return model_class.objects.filter(work_reltn__applicant_reltn=self.work_reltn.applicant_reltn).count()

        if hasattr(self, 'project_reltn'):
            return model_class.objects.filter(project_reltn__applicant_reltn=self.project_reltn.applicant_reltn).count()

        raise ValidationError("Cannot count related objects for this model.")

    def check_record_limit(self): 
        
        if self.pk and self.__class__.objects.filter(pk=self.pk).exists():
            return 
        
        plan = self.get_plan()
        
        from django.contrib.contenttypes.models import ContentType
        content_type = ContentType.objects.get_for_model(self.__class__)
        limit = RecordLimit.objects.filter(plan=plan, content_type=content_type).first()

        if limit and self.get_existing_count() >= limit.max_records:
            raise ValidationError( f"Limit of {limit.max_records} {self.__class__.__name__} records reached for your plan.")
        
    def save(self, *args, **kwargs):
        self.check_record_limit()
        super().save(*args, **kwargs)
        
    
    """I dont feel like dealing with this tbh it runs before save so we hit check_record_limit twice...owell atm"""
    def clean(self):
        super().clean()
        self.check_record_limit()
    