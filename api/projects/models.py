from django.db import models
from api.applicant.models import Applicant
from common.pk_generator import generate_id
# Create your models here.
class Project(models.Model):
    id = models.CharField(
        max_length=37,
        primary_key=True,
        editable=False,
        default=generate_id
        )
    applicant_reltn = models.ForeignKey(Applicant,on_delete=models.CASCADE)
    name = models.CharField(max_length=75)
    demo_url = models.URLField(null=True,blank=True)
    source_control_url = models.URLField(null=True,blank=True)
    description = models.TextField(max_length=500,blank=True,null=True)
    
    def __str__(self):
        return self.name

class ProjectDetails(models.Model):
    id = models.CharField(
        max_length=37,
        primary_key=True,
        editable=False,
        default=generate_id
        )
    project_reltn = models.ForeignKey(Project,on_delete=models.CASCADE)
    detail_text = models.CharField(max_length=255,blank=True,null=True)
    detail_image = models.URLField(blank=True,null=True)
    
    def __str__(self):
        return self.project_reltn.name