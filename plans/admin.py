from django.contrib import admin
from .models import Plan,RecordLimit
# Register your models here.
@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):

    def get_readonly_fields(self, request, obj=None):
        if obj: 
            return ('name',)
        return ()

@admin.register(RecordLimit)
class RecordLimitAdmin(admin.ModelAdmin):
    list_display=('plan','content_type','max_records')