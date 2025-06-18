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
    
    @staticmethod
    def getWorkInformationObj(applicant):
        work_queryset = WorkHistory.objects.filter(applicant_reltn=applicant).prefetch_related('work_details').order_by('order')
        work_list = []
        for work in work_queryset:
            work_details = list(work.work_details.all())
            work_list.append({
                "work": work,
                "details": work_details
            })
        return work_list
    
    @staticmethod
    def getWorkInformationSerialized(applicant):
        from .serializers import WorkHistorySerializer,WorkHistoryDetailsSerializer
        work_queryset = WorkHistory.objects.filter(applicant_reltn=applicant).prefetch_related('work_details').order_by('order')
        work_list = []
        for work in work_queryset:
            work_list.append({
                "work": WorkHistorySerializer(work).data,
                "details": WorkHistoryDetailsSerializer(work.work_details.all(), many=True).data
            })
        return work_list
    
    def __str__(self):
        return self.employer_name
    
class WorkHistoryDetails(models.Model):
    id = models.CharField(
        max_length=37,
        primary_key=True,
        editable=False,
        default=generate_id
        )
    work_reltn = models.ForeignKey(WorkHistory,on_delete=models.CASCADE,related_name='work_details')
    work_detail_text = models.CharField(max_length=255)
    order = models.PositiveIntegerField(default=100)
    active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.work_reltn.employer_name