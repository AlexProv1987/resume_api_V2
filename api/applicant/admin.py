from django.contrib import admin
from .models import Applicant,ApplicantContactMethods,ApplicantSocials
from user.models import User
from django.utils.translation import gettext_lazy as _
from .forms import ApplicantSocialsForm,ApplicantContactForm

# Register your models here.
@admin.register(Applicant)
class ApplicantAdmin(admin.ModelAdmin):
    list_per_page=20
    
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
    
@admin.register(ApplicantSocials)
class ApplicantSocialsAdmin(admin.ModelAdmin):
    list_per_page=20
    list_display=('platform','applicant_reltn','order','show',)
    list_editable=('order','show',)
    
    form=ApplicantSocialsForm
    
    fields=('applicant_reltn',
            'platform',
            'url',
            'order',
            'show',
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
        return [f for f in fields if f != 'applicant_reltn']
    
    def get_readonly_fields(self, request, obj=None):
        if obj: 
            return ('applicant_reltn',)
        return ()
    
    def get_form(self, request, obj=None, **kwargs):
        '''Never Ask me about this again...unique together is applied at db level..not form'''
        '''return custom form class passing in the request to evaluate if we need to set the applicant_reltn'''
        '''defaulting is now handled in there in the reverse case since we have access to the request'''
        Form = super().get_form(request, obj, **kwargs)
        class RequestWrappedForm(Form):
            def __new__(cls, *args, **kw):
                kw['request'] = request
                return Form(*args, **kw)
        return RequestWrappedForm
    
        
@admin.register(ApplicantContactMethods)
class ApplicantContactMethodAdmin(admin.ModelAdmin):
    list_per_page=20
    list_display=('contact_type','applicant_reltn','order','show',)
    list_editable=('order','show',)
    
    form=ApplicantContactForm
    
    fields=('applicant_reltn',
            'contact_type',
            'value',
            'order',
            'show',
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
        return [f for f in fields if f != 'applicant_reltn']
    
    def get_readonly_fields(self, request, obj=None):
        if obj: 
            return ('applicant_reltn',)
        return ()
    
    def get_form(self, request, obj=None, **kwargs):
        '''Never Ask me about this again...unique together is applied at db level..not form'''
        '''return custom form class passing in the request to evaluate if we need to set the applicant_reltn'''
        '''defaulting is now handled in there in the reverse case since we have access to the request'''
        Form = super().get_form(request, obj, **kwargs)
        class RequestWrappedForm(Form):
            def __new__(cls, *args, **kw):
                kw['request'] = request
                return Form(*args, **kw)
        return RequestWrappedForm