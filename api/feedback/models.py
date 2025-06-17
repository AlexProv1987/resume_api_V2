from django.db import models
from api.applicant.models import Applicant
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.
class ApplicantFeedBack(models.Model):
    applicant_reltn = models.ForeignKey(Applicant,on_delete=models.CASCADE)
    rating=models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
    comment=models.TextField(max_length=2000,null=True,blank=True)
    full_name = models.CharField(max_length=75)
    phone_number=models.CharField(max_length=11)
    email=models.EmailField()
    company=models.CharField(max_length=125,null=True,blank=True)
    ip_address=models.GenericIPAddressField()
    user_agent=models.TextField(blank=True,null=True)
    created_at=models.DateTimeField(auto_now_add=True)