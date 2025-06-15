from django.db import models
from api.applicant.models import Applicant
from common.pk_generator import generate_id

# Create your models here.
class WorkHistory(models.Model):
    id = models.CharField(
        max_length=37,
        primary_key=True,
        editable=False,
        default=generate_id
        )
    employer_name = models.CharField(max_length=100)
    job_title = models.CharField(max_length=50)
    applicant_reltn = models.ForeignKey(Applicant,on_delete=models.CASCADE)
    from_date = models.DateField()
    to_date = models.DateField(null=True,blank=True)
    current_employer = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=100)
    active = models.BooleanField(default=True)
    
class WorkHistoryDetails(models.Model):
    id = models.CharField(
        max_length=37,
        primary_key=True,
        editable=False,
        default=generate_id
        )
    work_reltn = models.ForeignKey(WorkHistory,on_delete=models.CASCADE)
    work_detail_text = models.CharField(max_length=255)
    order = models.PositiveIntegerField(default=100)
    active = models.BooleanField(default=True)