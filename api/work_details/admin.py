from django.contrib import admin
from .models import *
from django.core.exceptions import ValidationError
from .filters import UserRestrictedWorkFilter
# Register your models here.
@admin.register(WorkHistory)
class WorkHistoryAdmin(admin.ModelAdmin):
    list_display=('employer_name','applicant_reltn','order',)
    search_fields=('employer_name',)
    search_help_text='Search By Employer Name'
    list_editable=('order',)
    fields = ('applicant_reltn',
              'employer_name',
              'job_title',
              'from_date',
              'to_date',
              'order',
              'current_employer',
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
    
    def get_readonly_fields(self, request, obj=None):
        if obj: 
            return ('applicant_reltn',)
        return ()
    
    def save_model(self, request, obj, form, change):
        
        if not request.user.is_superuser:
            try:
                applicant = Applicant.objects.get(user_reltn=request.user)
            except Applicant.DoesNotExist:
                raise ValidationError("No Applicant profile is associated with this user.")
            
            obj.applicant_reltn = applicant
            
        super().save_model(request, obj, form, change)

@admin.register(WorkHistoryDetails)
class WorkHistoryDetailsAdmin(admin.ModelAdmin):
    list_per_page=20
    list_editable=('order',)
    list_display=('work_reltn','order',)
    search_fields=('work_reltn__employer_name',)
    search_help_text='Search By Employer Name'
    list_filter=(UserRestrictedWorkFilter,)
    
    fields = ('work_reltn',
              'work_detail_text',
              'order',
              'active',
              )
    
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
           return qs
        return qs.filter(work_reltn__applicant_reltn__user_reltn=request.user).order_by('work_reltn__employer_name','order')
        
    
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "project_reltn":
            if not request.user.is_superuser:
                kwargs["queryset"] = WorkHistory.objects.filter(applicant_reltn__user_reltn=request.user)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
