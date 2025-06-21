from django.contrib import admin
from .models import Plan,RecordLimit
# Register your models here.
admin.site.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    pass

admin.site.register(RecordLimit)
class RecordLimitAdmin(admin.ModelAdmin):
    pass