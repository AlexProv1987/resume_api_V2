from django.contrib.admin import SimpleListFilter
from .models import WorkHistory 
class UserRestrictedWorkFilter(SimpleListFilter):
    title = 'Project Name'
    parameter_name = 'project'

    def lookups(self, request, model_admin):
        qs = WorkHistory.objects.all()
        if not request.user.is_superuser:
            qs = qs.filter(applicant_reltn__user_reltn=request.user)
        return [(p.id, p.employer_name) for p in qs]

    def queryset(self, request, queryset):
        value = self.value()
        if value:
            return queryset.filter(work_reltn__id=value)
        return queryset