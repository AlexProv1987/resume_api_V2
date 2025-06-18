from django.contrib import admin
from .models import Applicant
from api.user.models import User
from django.utils.translation import gettext_lazy as _
# Register your models here.
@admin.register(Applicant)
class CustomerApplicantManager(admin.ModelAdmin):
    fields=('user_reltn',
            'current_title',
            'banner_img',
            'applicant_photo',
            'applicant_bio',
            'accepting_work',
            )
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
           return qs
        return qs.filter(user_reltn=request.user)
    
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "user_reltn" and not request.user.is_superuser:
            kwargs["queryset"] = User.objects.filter(pk=request.user.id)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
    
    def get_readonly_fields(self, request, obj=None):
        if obj: 
            return ('user_reltn',)
        return ()