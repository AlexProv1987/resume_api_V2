from rest_framework.generics import ListAPIView
from .serializers import *
from .models import *
# Create your views here.
class GetApplicantSkills(ListAPIView):
    serializer_class=SkillSerializer
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def get_queryset(self):
        queryset = Skill.objects.filter(applicant_reltn=self.request.query_params.get('applicant',None))
        return queryset
    
class GetApplicantEducation(ListAPIView):
    serializer_class=EducationSerializer
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def get_queryset(self):
        queryset = Education.objects.filter(applicant_reltn=self.request.query_params.get('applicant',None))
        return queryset
    
class GetApplicantCertifications(ListAPIView):
    serializer_class=CertificationSerializer
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def get_queryset(self):
        queryset = Certification.objects.filter(applicant_reltn=self.request.query_params.get('applicant',None))
        return queryset
     
class GetApplicantReferences(ListAPIView):
    serializer_class=ReferencesSerializer
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def get_queryset(self):
        queryset = References.objects.filter(applicant_reltn=self.request.query_params.get('applicant',None))
        return queryset
    
class GetApplicantAdditionalContext(ListAPIView):
    serializer_class=AdditionalContextSerializer
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def get_queryset(self):
        queryset = AdditionalContext.objects.filter(applicant_reltn=self.request.query_params.get('applicant',None))
        return queryset
      