from rest_framework.generics import ListAPIView
from .serializers import *
from .models import *
from common.mixins.plan_limit_mixin import EnforcePlanLimitMixin
from plans.models import RecordLimit
# Create your views here.
class GetApplicantSkills(EnforcePlanLimitMixin,ListAPIView):
    serializer_class=SkillSerializer
    queryset=Skill.objects.all()
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    
class GetApplicantEducation(EnforcePlanLimitMixin,ListAPIView):
    serializer_class=EducationSerializer
    queryset=Education.objects.all()
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    
class GetApplicantCertifications(EnforcePlanLimitMixin,ListAPIView):
    serializer_class=CertificationSerializer
    queryset=Certification.objects.all()
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
   
     
class GetApplicantReferences(EnforcePlanLimitMixin,ListAPIView):
    serializer_class=ReferencesSerializer
    queryset=References.objects.all()
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
   
    
class GetApplicantAwards(EnforcePlanLimitMixin,ListAPIView):
    serializer_class=AwardsSerializer
    queryset=Awards.objects.all()
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
  
    
class GetApplicantAdditionalContext(EnforcePlanLimitMixin,ListAPIView):
    serializer_class=AdditionalContextSerializer
    queryset=AdditionalContext.objects.all()
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    