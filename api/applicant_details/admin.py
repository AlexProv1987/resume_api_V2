from django.contrib import admin
from .models import *
from django.core.exceptions import ValidationError
from django import forms

# Register your models here.
@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
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
    
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
           return qs
        return qs.filter(applicant_reltn__user_reltn=request.user).order_by('order')
        
    def get_fields(self, request, obj=None):
        fields = super().get_fields(request, obj)
        if request.user.is_superuser:
            return fields
        return [f for f in fields if f != 'applicant_reltn']
    
    def save_model(self, request, obj, form, change):
        
        if not request.user.is_superuser:
            try:
                applicant = Applicant.objects.get(user_reltn=request.user)
            except Applicant.DoesNotExist:
                raise ValidationError("No Applicant profile is associated with this user.")
            
            obj.applicant_reltn = applicant
            
        super().save_model(request, obj, form, change)
        
    def get_readonly_fields(self, request, obj=None):
        if obj: 
            return ('applicant_reltn',)
        return ()
    
@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    
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
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
           return qs
        return qs.filter(applicant_reltn__user_reltn=request.user).order_by('order')
    
    def get_fields(self, request, obj=None):
        fields = super().get_fields(request, obj)
        if request.user.is_superuser:
            return fields
        return [f for f in fields if f != 'applicant_reltn']
    
    def save_model(self, request, obj, form, change):
        
        if not request.user.is_superuser:
            try:
                applicant = Applicant.objects.get(user_reltn=request.user)
            except Applicant.DoesNotExist:
                raise ValidationError("No Applicant profile is associated with this user.")
            
            obj.applicant_reltn = applicant
            
        super().save_model(request, obj, form, change)
        
    def get_readonly_fields(self, request, obj=None):
        if obj: 
            return ('applicant_reltn',)
        return ()
    
@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
    
    list_display=('name','applicant_reltn','order',)
    search_fields=('name',)
    search_help_text='Search By Certification Name'
    list_editable=('order',)
    
    fields=('applicant_reltn',
            'name',
            'attained_on',
            'order',
            )
    
    def get_fields(self, request, obj=None):
        fields = super().get_fields(request, obj)
        if request.user.is_superuser:
            return fields
        return [f for f in fields if f != 'applicant_reltn']
    
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
           return qs
        return qs.filter(applicant_reltn__user_reltn=request.user).order_by('order')
    
    def save_model(self, request, obj, form, change):
        
        if not request.user.is_superuser:
            try:
                applicant = Applicant.objects.get(user_reltn=request.user)
            except Applicant.DoesNotExist:
                raise ValidationError("No Applicant profile is associated with this user.")
            
            obj.applicant_reltn = applicant
            
        super().save_model(request, obj, form, change)
        
    def get_readonly_fields(self, request, obj=None):
        if obj: 
            return ('applicant_reltn',)
        return ()
     
@admin.register(References)
class ReferencesAdmin(admin.ModelAdmin):
    
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
    
    def get_fields(self, request, obj=None):
        fields = super().get_fields(request, obj)
        if request.user.is_superuser:
            return fields
        return [f for f in fields if f != 'applicant_reltn']
    
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
           return qs
        return qs.filter(applicant_reltn__user_reltn=request.user).order_by('order')
    
    def save_model(self, request, obj, form, change):
        
        if not request.user.is_superuser:
            try:
                applicant = Applicant.objects.get(user_reltn=request.user)
            except Applicant.DoesNotExist:
                raise ValidationError("No Applicant profile is associated with this user.")
            
            obj.applicant_reltn = applicant
            
        super().save_model(request, obj, form, change)
        
    def get_readonly_fields(self, request, obj=None):
        if obj: 
            return ('applicant_reltn',)
        return ()

@admin.register(Awards)
class AwardsAdmin(admin.ModelAdmin):
    
    list_display=('reward_name','applicant_reltn','order')
    search_fields=('reward_name',)
    search_help_text='Search By Award Name'
    list_editable=('order',)
    
    fields=('applicant_reltn',
            'reward_name',
            'reward_descrption',
            'order',
            )
    
    def get_fields(self, request, obj=None):
        fields = super().get_fields(request, obj)
        if request.user.is_superuser:
            return fields
        return [f for f in fields if f != 'applicant_reltn']
    
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
           return qs
        return qs.filter(applicant_reltn__user_reltn=request.user).order_by('order')
    
    def save_model(self, request, obj, form, change):
        
        if not request.user.is_superuser:
            try:
                applicant = Applicant.objects.get(user_reltn=request.user)
            except Applicant.DoesNotExist:
                raise ValidationError("No Applicant profile is associated with this user.")
            
            obj.applicant_reltn = applicant
            
        super().save_model(request, obj, form, change)
        
    def get_readonly_fields(self, request, obj=None):
        if obj: 
            return ('applicant_reltn',)
        return ()
      
@admin.register(AdditionalContext)
class AdditionalContextAdmin(admin.ModelAdmin):
    list_display=('applicant_reltn','context_text','active')

    fields=('applicant_reltn',
            'context_text',
            'active',
            )
    
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
        form.base_fields['context_text'].widget = forms.Textarea(attrs={'rows': 3, 'cols': 80})
        
        return form
    def save_model(self, request, obj, form, change):
        
        if not request.user.is_superuser:
            try:
                applicant = Applicant.objects.get(user_reltn=request.user)
            except Applicant.DoesNotExist:
                raise ValidationError("No Applicant profile is associated with this user.")
            
            obj.applicant_reltn = applicant
            
        super().save_model(request, obj, form, change)
        
    def get_readonly_fields(self, request, obj=None):
        if obj: 
            return ('applicant_reltn',)
        return ()
