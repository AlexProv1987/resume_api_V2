from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
# Register your models here.
@admin.register(User)
class CustomerUserManager(UserAdmin):
    
    list_display=('username',
                  'first_name',
                  'last_name',
                )
    
    def get_fieldsets(self, request, obj=None):
        if request.user.is_superuser:
            return super().get_fieldsets(request, obj)

        return (
            (None, {"fields": ("username", "password")}),
            (_("Personal info"), {"fields": ("first_name", "last_name", "email")}),
        )
        
    def get_list_filter(self, request):
        if request.user.is_superuser:
            return super().get_list_filter(request)
        return ()
    
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
           return qs
        return qs.filter(pk=request.user.id)