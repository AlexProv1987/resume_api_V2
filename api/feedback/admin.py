from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(ApplicantFeedBack)
class ApplicantFeedBackAdmin(admin.ModelAdmin):
    
    list_display=('applicant_reltn__user_reltn__first_name',)
    
    def get_readonly_fields(self, request, obj=None):
        return [field.name for field in self.model._meta.concrete_fields]
    
    def has_add_permission(self, request):
            return False
