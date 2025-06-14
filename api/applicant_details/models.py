from django.db import models
from api.applicant.models import Applicant
from common.pk_generator import generate_id

# Create your models here.
class Skill(models.Model):
    id = models.CharField(
        max_length=37,
        primary_key=True,
        editable=False,
        default=generate_id
        )
    applicant_reltn = models.ForeignKey(Applicant,on_delete=models.CASCADE)
    skill_name = models.CharField(max_length=50)
    skill_description = models.CharField(max_length=255,blank=True,null=True)
    years_of_experience = models.PositiveIntegerField(default=0)
    def __str__(self):
        return self.skill_name
    
class Education(models.Model):
    id = models.CharField(
        max_length=37,
        primary_key=True,
        editable=False,
        default=generate_id
        )
    applicant_reltn = models.ForeignKey(Applicant,on_delete=models.CASCADE)
    #create choices
    education_level = models.CharField(max_length=255)
    area_of_study = models.CharField(max_length=50,null=True,blank=True)
    name = models.CharField(max_length=255)
    from_date = models.DateField(blank=False,null=False)
    to_date = models.DateField()
    currently_attending = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name
    
class Certification(models.Model):
    id = models.CharField(
        max_length=37,
        primary_key=True,
        editable=False,
        default=generate_id
        )
    applicant_reltn = models.ForeignKey(Applicant,on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    attained_on = models.DateField(null=False)
    
    def __str__(self):
        return self.name
    
class References(models.Model):
    id = models.CharField(
        max_length=37,
        primary_key=True,
        editable=False,
        default=generate_id
        )
    applicant_reltn = models.ForeignKey(Applicant,on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    relation = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
    
class AdditionalContext(models.Model):
    id = models.CharField(
        max_length=37,
        primary_key=True,
        editable=False,
        default=generate_id
        )
    applicant_reltn = models.ForeignKey(Applicant,on_delete=models.CASCADE)
    context_text = models.CharField(max_length=255)
    
    def __str__(self):
        return f"{self.applicant_reltn.user_reltn.first_name} {self.applicant_reltn.user_reltn.last_name}" 
    