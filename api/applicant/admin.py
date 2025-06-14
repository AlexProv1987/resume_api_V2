from django.contrib import admin
from .models import Applicant
# Register your models here.
@admin.register(Applicant)
class CustomerApplicantManager(admin.ModelAdmin):
    pass