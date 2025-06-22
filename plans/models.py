from django.db import models
from django.contrib.contenttypes.models import ContentType

# Create your models here.
class Plan(models.Model):
    name = models.CharField(max_length=100,unique=True,db_index=True)
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    monthly_fee = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    
    def __str__(self):
        return self.name
    
    @staticmethod
    def get_default_plan():
        try:
            return Plan.objects.get(name="Free").id
        except Plan.DoesNotExist:
            return None
    
class RecordLimit(models.Model):
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE, related_name='limits')
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE) 
    max_records = models.PositiveIntegerField()
    
    class Meta:
        unique_together = ('plan', 'content_type')
        
    def get_model_class(self):
        return self.content_type.model_class()