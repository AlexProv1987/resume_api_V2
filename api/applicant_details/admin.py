from django.contrib import admin
from .models import *
from django.core.exceptions import ValidationError
from django import forms
from .forms import ApplicantDetailsForm
# Register your models here.
class ApplicantDetailsBaseAdmin(admin.ModelAdmin):
    form = ApplicantDetailsForm
    def get_fields(self, request, obj=None):
        fields = super().get_fields(request, obj)
        if request.user.is_superuser:
            return fields
        return [f for f in fields if f != 'applicant_reltn']
    
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
           return qs
        return qs.filter(applicant_reltn__user_reltn=request.user)
    
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        class FormWithRequest(form):
            def __new__(cls, *args, **kw):
                kw['request'] = request
                return form(*args, **kw)
        return FormWithRequest
        
    def get_readonly_fields(self, request, obj=None):
        if obj: 
            return ('applicant_reltn',)
        return ()
    
@admin.register(Skill)
class SkillAdmin(ApplicantDetailsBaseAdmin):
    
    list_display=('skill_name','applicant_reltn','order',)
    search_fields=('skill_name',)
    search_help_text='Search By Skill Name'
    list_editable=('order',)
    fields = ('applicant_reltn',
              'skill_name',
              'skill_description',
              'skill_logo',
              'years_of_experience',
              'order',
              )
    
@admin.register(Education)
class EducationAdmin(ApplicantDetailsBaseAdmin):
    
    list_display=('name','applicant_reltn','order',)
    search_fields=('name',)
    search_help_text='Search By Institution Name'
    list_editable=('order',)
    fields = ('applicant_reltn',
              'name',
              'education_level',
              'area_of_study',
              'from_date',
              'to_date',
              'order',
              'currently_attending',
            )
    
@admin.register(Certification)
class CertificationAdmin(ApplicantDetailsBaseAdmin):
    
    list_display=('name','applicant_reltn','order',)
    search_fields=('name',)
    search_help_text='Search By Certification Name'
    list_editable=('order',)
    
    fields=('applicant_reltn',
            'name',
            'attained_on',
            'order',
            )
     
@admin.register(References)
class ReferencesAdmin(ApplicantDetailsBaseAdmin):
    
    list_display=('name','applicant_reltn','order',)
    search_fields=('name',)
    search_help_text='Search By Reference Name'
    list_editable=('order',)
    
    fields=('applicant_reltn',
            'name',
            'relation',
            'job_title',
            'reference_recommendation',
            'order',
            )

@admin.register(Awards)
class AwardsAdmin(ApplicantDetailsBaseAdmin):
    
    list_display=('reward_name','applicant_reltn','order')
    search_fields=('reward_name',)
    search_help_text='Search By Award Name'
    list_editable=('order',)
    
    fields=('applicant_reltn',
            'reward_name',
            'reward_descrption',
            'order',
            )
      
@admin.register(AdditionalContext)
class AdditionalContextAdmin(ApplicantDetailsBaseAdmin):
    list_display=('applicant_reltn','context_text','active')
    list_editable=('active',)
    
    fields=('applicant_reltn',
            'context_text',
            'active',
            )