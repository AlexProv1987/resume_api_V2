from django.core.exceptions import ValidationError
from django import forms
from api.applicant.models import Applicant

class ApplicantDetailsForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super().clean()
        if not self.instance.applicant_reltn_id and self.request and not self.request.user.is_superuser:
            try:
                applicant = Applicant.objects.get(user_reltn=self.request.user)
                cleaned_data['applicant_reltn'] = applicant
                self.instance.applicant_reltn = applicant
            except Applicant.DoesNotExist:
                raise ValidationError("No Applicant profile is associated with this user.")
        return cleaned_data