from django.contrib import admin
from .models import *
from django.core.exceptions import ValidationError
# Register your models here.
@admin.register(ApplicantFeedBack)
class ApplicantFeedBackAdmin(admin.ModelAdmin):
    list_display=('rating','comment','full_name','created_at')
    search_fields=('skill_name',)
    search_help_text='Search By Skill Name'
    
    fields = ('applicant_reltn',
              'rating',
              'comment',
              'full_name',
              'email',
              'company',
              'ip_address',
              'user_agent',
              'created_at',
              )
    
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
           return qs
        return qs.filter(applicant_reltn__user_reltn=request.user)
        
    def get_fields(self, request, obj=None):
        fields = super().get_fields(request, obj)
        if request.user.is_superuser:
            return fields
        return [f for f in fields if f not in ('applicant_reltn','ip_address','user_agent')]
    
    def get_readonly_fields(self, request, obj=None):
        if request.user.is_superuser:
            return ('created_at',)
        return [f.name for f in self.model._meta.fields]