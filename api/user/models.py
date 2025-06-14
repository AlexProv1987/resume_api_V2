from django.db import models
from django.contrib.auth.models import AbstractUser
from common.pk_generator import generate_id

class User(AbstractUser):
    id = models.CharField(
        max_length=37,
        primary_key=True,
        editable=False,
        default=generate_id)
    first_name = models.CharField(max_length=150, blank=False,null=False)
    last_name = models.CharField(max_length=150, blank=False,null=False)
    email = models.EmailField(unique=True,blank=False,null=False)
    phone_number = models.CharField(max_length=20,blank=True,null=True)
