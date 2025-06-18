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
    video_url = models.URLField(null=True,blank=True)
    description = models.TextField(max_length=500,blank=True,null=True)
    order = models.PositiveIntegerField(default=100)
    
    @staticmethod
    def getProjectInfoObj(applicant):
        project_queryset = Project.objects.filter(applicant_reltn=applicant).prefetch_related('project_details').order_by('order')
        project_list = []
        for project in project_queryset:
            project_details = list(project.project_details.all().order_by('order')) 
            project_list.append({
                "project": project,
                "details": project_details
            })
        return project_list
    
    @staticmethod
    def getProjectInfoSerialized(applicant):
        from .serializers import ProjectSerializer,ProjectDetailsSerializer
        project_queryset = Project.objects.filter(applicant_reltn=applicant).prefetch_related('project_details').order_by('order')
        project_list = []
        for project in project_queryset:
            project_list.append({
                "project": ProjectSerializer(project).data,
                "details": ProjectDetailsSerializer(project.project_details.all().order_by('order'), many=True).data
            })
        return project_list
    
    def __str__(self):
        return self.name

class ProjectDetails(models.Model):
    id = models.CharField(
        max_length=37,
        primary_key=True,
        editable=False,
        default=generate_id
        )
    project_reltn = models.ForeignKey(Project,on_delete=models.CASCADE, related_name='project_details')
    detail_text = models.CharField(max_length=255,blank=True,null=True)
    detail_image = models.URLField(blank=True,null=True)
    order = models.PositiveIntegerField(default=100)
    
    def __str__(self):
        return self.project_reltn.name