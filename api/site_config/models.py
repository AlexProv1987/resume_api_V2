from django.db import models
from api.applicant.models import Applicant
"""Leaving this in place but leaving alone for now."""
#pip install django-admin-sortable2
#region developer controlled    
class Page(models.Model):
    name = models.CharField(max_length=50, unique=True, db_index=True)
    advanced_config = models.JSONField(blank=True, null=True,help_text="Optional: JSON to override or extend base config.")
    
    def __str__(self):
        return self.name
    
class Widget(models.Model):
    name = models.CharField(max_length=50, unique=True, db_index=True)
    advanced_config = models.JSONField(blank=True, null=True,help_text="Optional: JSON to override or extend base config.")
    
    def __str__(self):
        return self.name
    
class PageWidget(models.Model):
    class WidgetRegion(models.TextChoices):
        LEFT = "left", "Left Column"
        RIGHT = "right", "Right Column"
        FOOTER = "footer", "Footer"

    page = models.ForeignKey(Page, related_name='widgets', on_delete=models.CASCADE)
    widget = models.ForeignKey(Widget, on_delete=models.CASCADE)
    location = models.CharField(max_length=20, choices=WidgetRegion.choices, default=WidgetRegion.RIGHT)

    class Meta:
        unique_together = ('page', 'widget')
    

#endregion

#region applicant controlled

#applicants page level config
class PageOption(models.Model):
    applicant_reltn = models.ForeignKey(Applicant, on_delete=models.CASCADE, related_name='page_options')
    page = models.ForeignKey(Page, on_delete=models.CASCADE)
    preferences = models.JSONField(default=dict,help_text="Optional: JSON to override or extend base config.")
    class Meta:
        unique_together = ('applicant_reltn', 'page')   
    

#applicant 
class ApplicantWidget(models.Model):
    applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE, related_name='widget_orders')
    page = models.ForeignKey(Page, on_delete=models.CASCADE)
    widget = models.ForeignKey(Widget, on_delete=models.CASCADE)

    display_order = models.PositiveIntegerField(default=0)
    is_visible = models.BooleanField(default=True)

    class Meta:
        unique_together = ('applicant', 'page', 'widget')
        ordering = ['display_order']     
        
#Applicant’s customization of each widget (on a page)
class WidgetInstanceOption(models.Model):
    applicant_reltn = models.ForeignKey(Applicant, on_delete=models.CASCADE, related_name='widget_instance_options')
    widget = models.ForeignKey(Widget, on_delete=models.CASCADE)

    title_override = models.CharField(max_length=200, blank=True, null=True)
    is_visible = models.BooleanField(default=True)
    other_config = models.JSONField(blank=True, null=True)

    class Meta:
        unique_together = ('applicant_reltn', 'widget')
#end region