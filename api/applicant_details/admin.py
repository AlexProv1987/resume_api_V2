from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    pass

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    pass

@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
    pass

@admin.register(References)
class ReferencesAdmin(admin.ModelAdmin):
    pass

@admin.register(AdditionalContext)
class AdditionalContextAdmin(admin.ModelAdmin):
    pass