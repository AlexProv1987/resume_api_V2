from django.db import models
from api.applicant.models import Applicant
from common.pk_generator import generate_id
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator, MaxValueValidator
from plans.mixins import EnforceRecordLimitMixin
# Create your models here.
class WorkHistory(EnforceRecordLimitMixin,models.Model):
    id = models.CharField(
        max_length=37,
        primary_key=True,
        editable=False,
        default=generate_id
        )
    applicant_reltn = models.ForeignKey(Applicant,
                                        on_delete=models.CASCADE,
                                        verbose_name=_('Applicant'),
                                        related_name='work')
    employer_name = models.CharField(max_length=100,verbose_name=_('Employer Name'))
    job_title = models.CharField(max_length=50,verbose_name=_('Job Title'))
    from_date = models.DateField(verbose_name=_('Start Date'))
    to_date = models.DateField(null=True,blank=True,verbose_name=_('End Date'))
    current_employer = models.BooleanField(default=False,verbose_name=_('Current Employer'))
    order = models.PositiveIntegerField(default=100,validators=[MinValueValidator(1), MaxValueValidator(1000)])

    class Meta:
        ordering = ['order']
        
    @staticmethod
    def getWorkInformationObj(applicant):
        work_queryset = WorkHistory.objects.filter(applicant_reltn=applicant).prefetch_related('work_details').order_by('order')
        work_list = []
        for work in work_queryset:
            work_details = list(work.work_details.all().order_by('order'))
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
                "details": WorkHistoryDetailsSerializer(work.work_details.all().order_by('order'), many=True).data
            })
        return work_list
    
    def __str__(self):
        return self.employer_name
    
    class Meta:
        verbose_name_plural=_('Employer')
        ordering = ['order']
        
class WorkHistoryDetails(EnforceRecordLimitMixin,models.Model):
    id = models.CharField(
        max_length=37,
        primary_key=True,
        editable=False,
        default=generate_id
        )
    work_reltn = models.ForeignKey(WorkHistory,on_delete=models.CASCADE,related_name='work_details',verbose_name=_('Employer'))
    work_detail_text = models.CharField(max_length=255,verbose_name=_('Description'), help_text=_('These are your work bullet points on a resume.'))
    order = models.PositiveIntegerField(default=100,validators=[MinValueValidator(1), MaxValueValidator(1000)])
    active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.work_reltn.employer_name
        
    class Meta:
        verbose_name_plural=_('Employment Details')
        ordering = ['order']