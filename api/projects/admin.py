from django.contrib import admin
from .models import Project,ProjectDetails,Applicant
from django.core.exceptions import ValidationError
from .filters import UserRestrictedProjectFilter
# Register your models here.
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display=('name','applicant_reltn','order',)
    search_fields=('name',)
    search_help_text='Search By Project Name'
    list_editable=('order',)
    
    fields = ('applicant_reltn',
              'name',
              'demo_url',
              'source_control_url',
              'video_url',
              'description',
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
        
@admin.register(ProjectDetails)
class ProjectDetailsAdmin(admin.ModelAdmin):
    
    list_per_page=20
    list_editable=('order',)
    list_display=('project_reltn','order',)
    search_fields=('project_reltn__name',)
    search_help_text='Search By Project Name'
    list_filter=(UserRestrictedProjectFilter,)
    
    fields = ('project_reltn',
              'detail_image',
              'detail_text',
              'order',
              )
    
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
           return qs
        return qs.filter(project_reltn__applicant_reltn__user_reltn=request.user).order_by('project_reltn__name','order')
        
    
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "project_reltn":
            if not request.user.is_superuser:
                kwargs["queryset"] = Project.objects.filter(applicant_reltn__user_reltn=request.user)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)