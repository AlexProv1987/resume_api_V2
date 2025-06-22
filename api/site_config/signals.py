from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Applicant, Page, PageOption, Widget, PageWidget, ApplicantWidget
'''
Create a PageOption record for each defined Page

Create WidgetInstanceOption (if needed) for per-widget configs

Create ApplicantWidget records for each PageWidget — these hold visibility + display order
'''
@receiver(post_save, sender=Applicant)
def create_applicant_layout(sender, instance: Applicant, created, **kwargs):
    if not created:
        return 

    pages = Page.objects.all()
    for page in pages:
        PageOption.objects.get_or_create(applicant_reltn=instance, page=page)

        # Developer-defined widget layout
        page_widgets = PageWidget.objects.filter(page=page).select_related("widget")
        for idx, page_widget in enumerate(page_widgets):
            widget = page_widget.widget

            # Create per-applicant widget order
            ApplicantWidget.objects.get_or_create(
                applicant=instance,
                page=page,
                widget=widget,
                defaults={
                    'display_order': idx,
                    'is_visible': True,
                }
            )
