from django.contrib import admin
from .models import Page,PageOption,PageWidget,Widget,WidgetInstanceOption
# Register your models here.
admin.site.register(Page)
admin.site.register(PageOption)
admin.site.register(PageWidget)
admin.site.register(Widget)
admin.site.register(WidgetInstanceOption)

'''
from adminsortable2.admin import SortableAdminMixin

@admin.register(ApplicantWidget)
class ApplicantWidgetAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ['applicant', 'page', 'widget', 'is_visible']
'''