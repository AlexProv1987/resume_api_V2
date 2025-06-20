from django.db import models
from api.applicant.models import Applicant
from common.pk_generator import generate_id
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.
class Skill(models.Model):
    id = models.CharField(
        max_length=37,
        primary_key=True,
        editable=False,
        default=generate_id
        )
    applicant_reltn = models.ForeignKey(Applicant,
                                        on_delete=models.CASCADE,
                                        verbose_name=_('Applicant'),
                                        related_name='skills')
    skill_name = models.CharField(max_length=50,db_index=True,verbose_name=_('Skill'))
    skill_description = models.CharField(max_length=255,blank=True,null=True,verbose_name=_('Short Description'))
    years_of_experience = models.PositiveIntegerField(default=0,verbose_name=_('Years of Experience'))
    order=models.PositiveIntegerField(default=100,validators=[MinValueValidator(1), MaxValueValidator(1000)])
    skill_logo=models.URLField(blank=True,null=True,verbose_name=_('Logo'))
    
    def __str__(self):
        return self.skill_name
    
    class Meta:
        ordering = ['order']
        
class Education(models.Model):
    
    EDUCATION_LEVEL_CHOICES = [
    ("none", "No Formal Education"),
    ("primary", "Primary School"),
    ("middle", "Middle School"),
    ("high_school", "High School Diploma or GED"),
    ("associate", "Associate Degree"),
    ("vocational", "Vocational/Technical Certificate"),
    ("bachelor", "Bachelor's Degree"),
    ("post_bachelor", "Post-Bachelor Certificate"),
    ("master", "Master's Degree"),
    ("post_master", "Post-Master Certificate"),
    ("doctoral", "Doctoral Degree"),
    ("professional", "Professional Degree (MD, JD, etc.)"),
    ("other", "Other"),
    ]
    
    id = models.CharField(
        max_length=37,
        primary_key=True,
        editable=False,
        default=generate_id
        )
    applicant_reltn = models.ForeignKey(Applicant,
                                        on_delete=models.CASCADE,
                                        verbose_name=_('Applicant'),
                                        related_name='education')
    education_level = models.CharField(choices=EDUCATION_LEVEL_CHOICES,
                                       max_length=30,
                                       verbose_name=_('Education Level'))
    area_of_study = models.CharField(max_length=50,null=True,blank=True,db_index=True,verbose_name=_('Major'))
    name = models.CharField(max_length=255,verbose_name=_('Institution'))
    from_date = models.DateField(blank=False,null=False,verbose_name=_('Start Date'))
    to_date = models.DateField(verbose_name=_('End Date'))
    currently_attending = models.BooleanField(default=False,verbose_name=_('Attending'))
    order=models.PositiveIntegerField(default=100,validators=[MinValueValidator(1), MaxValueValidator(1000)])
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural=_('Education')
        ordering = ['order']
        
class Certification(models.Model):
    id = models.CharField(
        max_length=37,
        primary_key=True,
        editable=False,
        default=generate_id
        )
    applicant_reltn = models.ForeignKey(Applicant,on_delete=models.CASCADE,verbose_name=_('Applicant'),related_name='certifications')
    name = models.CharField(max_length=255,db_index=True,verbose_name=_('Certification Name'))
    attained_on = models.DateField(null=False,verbose_name=_('Recieved Date'))
    order=models.PositiveIntegerField(default=100,validators=[MinValueValidator(1), MaxValueValidator(1000)])
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['order']
        
class References(models.Model):
    id = models.CharField(
        max_length=37,
        primary_key=True,
        editable=False,
        default=generate_id
        )
    applicant_reltn = models.ForeignKey(Applicant,on_delete=models.CASCADE,verbose_name=_('Applicant'),related_name='references')
    name = models.CharField(max_length=255,db_index=True,verbose_name=_('Reference Full Name'))
    relation = models.CharField(max_length=255,verbose_name=_('Relation'))
    job_title=models.CharField(max_length=50,null=True,blank=True,verbose_name=_('Job Title'))
    order=models.PositiveIntegerField(default=100,validators=[MinValueValidator(1), MaxValueValidator(1000)])
    reference_recommendation = models.CharField(max_length=255,null=True,blank=True,verbose_name=_('Recommendation'))
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural=_('References')
        ordering = ['order']
        
class Awards(models.Model):
    id = models.CharField(
        max_length=37,
        primary_key=True,
        editable=False,
        default=generate_id
        )
    applicant_reltn = models.ForeignKey(Applicant,on_delete=models.CASCADE,verbose_name=_('Applicant'),related_name='awards')
    reward_name = models.CharField(max_length=50,db_index=True,verbose_name=_('Award Name'))
    reward_descrption = models.CharField(max_length=150,blank=True,null=True,verbose_name=_('Short Description'))
    order=models.PositiveIntegerField(default=100,validators=[MinValueValidator(1), MaxValueValidator(1000)])
    
    def __str__(self):
        return self.reward_name
    
    class Meta:
        verbose_name_plural=_('Awards')
        ordering = ['order']
        
class AdditionalContext(models.Model):
    id = models.CharField(
        max_length=37,
        primary_key=True,
        editable=False,
        default=generate_id
        )
    applicant_reltn = models.ForeignKey(Applicant,
                                        on_delete=models.CASCADE,
                                        verbose_name=_('Applicant'),
                                        related_name='context')
    context_text = models.CharField(max_length=255,
                                    verbose_name=_('Context'), 
                                    help_text=_("Additional Information you want to tell a LLM to know you more.")
                                )
    active = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.applicant_reltn.user_reltn.first_name} {self.applicant_reltn.user_reltn.last_name}" 

    class Meta:
        verbose_name_plural='LLM Context'
