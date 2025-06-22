from django.contrib import admin
from .models import *
from django.core.exceptions import ValidationError
from .filters import UserRestrictedWorkFilter
from api.applicant_details.admin import ApplicantDetailsBaseAdmin
# Register your models here.
@admin.register(WorkHistory)
class WorkHistoryAdmin(ApplicantDetailsBaseAdmin):
    list_display=('employer_name','applicant_reltn','job_title','order',)
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

@admin.register(WorkHistoryDetails)
class WorkHistoryDetailsAdmin(admin.ModelAdmin):
    list_per_page=20
    list_editable=('order',)
    list_display=('work_reltn','work_detail_text','order',)
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
