from django.db import models
from common.pk_generator import generate_id
from api.user.models import User
# Create your models here.
class Applicant(models.Model):
    id = models.CharField(
        max_length=37,
        primary_key=True,
        editable=False,
        default=generate_id
        )
    user_reltn = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='User')
    accepting_work = models.BooleanField(default=True,verbose_name='Open To Work')
    applicant_bio = models.TextField(max_length=3000, verbose_name='Biography')
    banner_img = models.URLField(null=True,blank=True)
    applicant_photo = models.URLField(null=True,blank=True)
    current_title = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.user_reltn.first_name}  {self.user_reltn.last_name}"
    