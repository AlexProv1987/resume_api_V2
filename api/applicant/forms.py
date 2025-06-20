from .models import Applicant,ApplicantSocials
from django import forms
from django.core.exceptions import ValidationError

class ApplicantSocialsForm(forms.ModelForm):
    class Meta:
        model = ApplicantSocials
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)

        if not self.request.user.is_superuser:
            self.fields.pop('applicant_reltn', None)

    def clean(self):
        cleaned_data = super().clean()
        platform = cleaned_data.get("platform")

        if not self.request.user.is_superuser:
            try:
                applicant = Applicant.objects.get(user_reltn=self.request.user)
                self.instance.applicant_reltn = applicant
            except Applicant.DoesNotExist:
                raise ValidationError("No applicant profile is associated with this user.")
            
        applicant = self.instance.applicant_reltn
        
        if applicant and platform:
            qs = ApplicantSocials.objects.filter(
                applicant_reltn=applicant,
                platform=platform
            )
            if self.instance.pk:
                qs = qs.exclude(pk=self.instance.pk)

            if qs.exists():
                raise ValidationError("This platform is already linked to this applicant.")
        
        return cleaned_data