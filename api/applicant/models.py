from django.db import models
from common.pk_generator import generate_id
from user.models import User
from django.db.models import Prefetch
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.
class Applicant(models.Model):
    id = models.CharField(
        max_length=37,
        primary_key=True,
        editable=False,
        default=generate_id
        )
    user_reltn = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name=_('User'))
    accepting_work = models.BooleanField(default=True,verbose_name=_('Open To Work'))
    applicant_bio = models.TextField(max_length=3000, verbose_name=_('Cover Letter'))
    banner_img = models.URLField(null=True,blank=True,verbose_name=_('Banner Image'))
    applicant_photo = models.URLField(null=True,blank=True,verbose_name=_('Photo'))
    current_title = models.CharField(max_length=50,null=True,blank=True,verbose_name=_('Current Title'))

    @staticmethod
    def get_applicant_resume(applicant_id:str):
        from api.work_details.models import WorkHistory
        from api.projects.models import Project
        from api.applicant_details.models import AdditionalContext
        aplicant=Applicant.objects.prefetch_related(
            'skills',
            'education',
            'certifications',
            'awards',
            'references',
            Prefetch(
              'context',
              queryset=AdditionalContext.objects.filter(active=True)  
            ),
            Prefetch(
                'social',
                queryset=ApplicantSocials.objects.filter(show=True)
            ),
            Prefetch(
                'contact_method',
                queryset=ApplicantContactMethods.objects.filter(show=True)
            ),
            Prefetch(
                'projects',
                queryset=Project.objects.prefetch_related('project_details')
            ),
            Prefetch(
                'work',
                queryset=WorkHistory.objects.prefetch_related('work_details')
            )
        ).get(pk=applicant_id)
        
        return aplicant
    
    @staticmethod
    def get_applicant_base_info(applicant_id:str):
        try:
            aplicant=Applicant.objects.prefetch_related(
                Prefetch(
                    'social',
                    queryset=ApplicantSocials.objects.filter(show=True)
                ),
                Prefetch(
                    'contact_method',
                    queryset=ApplicantContactMethods.objects.filter(show=True)
                ),
            ).get(pk=applicant_id)
            return aplicant
        except Applicant.DoesNotExist:
            return None
    
    def __str__(self):
        return f"{self.user_reltn.first_name}  {self.user_reltn.last_name}"

class ApplicantSocials(models.Model):
    SOCIAL_CHOICES = [
        ('linkedin', 'LinkedIn'),
        ('github', 'GitHub'),
        ('twitter', 'Twitter'),
        ('portfolio', 'Portfolio'),
        ('mastodon', 'Mastodon'),
        ('other', 'Other'),
    ]
    id = models.CharField(
        max_length=37,
        primary_key=True,
        editable=False,
        default=generate_id
        )
    applicant_reltn=models.ForeignKey(Applicant,on_delete=models.CASCADE,related_name='social',verbose_name=_('Applicant'))
    platform = models.CharField(max_length=20, choices=SOCIAL_CHOICES)
    url = models.URLField()
    show = models.BooleanField(default=True,db_index=True,help_text=_('Checked will display on resume web page.'))
    order = models.IntegerField(default=100,validators=[MinValueValidator(1), MaxValueValidator(1000)])
        
    class Meta:
        verbose_name_plural=_('Socials')
        unique_together = ('applicant_reltn', 'platform')
        ordering = ['order']
        
class ApplicantContactMethods(models.Model):
    
    CONTACT_TYPE_CHOICES = [
        ('email', 'Email'),
        ('phone', 'Phone'),
        ('whatsapp', 'WhatsApp'),
        ('signal', 'Signal'),
    ]
    id = models.CharField(
        max_length=37,
        primary_key=True,
        editable=False,
        default=generate_id
        )
    applicant_reltn=models.ForeignKey(Applicant,on_delete=models.CASCADE,related_name='contact_method',verbose_name=_('Applicant'))
    contact_type = models.CharField(max_length=20, choices=CONTACT_TYPE_CHOICES,verbose_name=_('Contact Type'))
    value = models.CharField(max_length=75)
    show = models.BooleanField(default=True,db_index=True,help_text=_('Checked will display on resume web page.'))
    order = models.IntegerField(default=100,validators=[MinValueValidator(1), MaxValueValidator(1000)])
    
    class Meta:
        verbose_name_plural=_('Contact Information')
        unique_together = ('applicant_reltn', 'contact_type')
        ordering = ['order']