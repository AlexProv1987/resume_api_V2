from django.db import models
from api.applicant.models import Applicant
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.translation import gettext_lazy as _
# Create your models here.
class ApplicantFeedBack(models.Model):
    applicant_reltn = models.ForeignKey(Applicant,on_delete=models.CASCADE,verbose_name=_('Applicant'))
    rating=models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)],verbose_name=_('Rating'))
    comment=models.TextField(max_length=2000,null=True,blank=True,verbose_name=_('Comment'))
    full_name = models.CharField(max_length=75,verbose_name=_('Name'))
    phone_number=models.CharField(max_length=11,verbose_name=_('Phone'))
    email=models.EmailField(null=True,blank=True,verbose_name=_('Email'))
    company=models.CharField(max_length=125,null=True,blank=True,verbose_name=_('Company'))
    ip_address=models.GenericIPAddressField(verbose_name=_('IP'))
    user_agent=models.TextField(blank=True,null=True,verbose_name=_('User Agent'))
    created_at=models.DateTimeField(auto_now_add=True,verbose_name=_('Created'))
    
    def __str__(self):
        return f"Feedback ({self.rating}/5) - {self.created_at.strftime('%b %d, %Y')}"

    class Meta:
        verbose_name_plural=_('Feedback')