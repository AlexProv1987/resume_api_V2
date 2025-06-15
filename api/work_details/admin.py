from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(WorkHistory)
class WorkHistoryAdmin(admin.ModelAdmin):
    list_display=('employer_name','job_title',)

@admin.register(WorkHistoryDetails)
class WorkHistoryDetailsAdmin(admin.ModelAdmin):
    pass
