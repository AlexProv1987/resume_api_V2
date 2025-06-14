from rest_framework.generics import ListAPIView
from .serializers import *
from .models import *
# Create your views here.
class GetProjects(ListAPIView):
    
    serializer_class=ProjectSerializer
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def get_queryset(self):
        queryset = Project.objects.filter(applicant_reltn=self.request.query_params.get('applicant',None))
        return queryset

class GetProjectDetails(ListAPIView):
    
    serializer_class=ProjectDetailsSerializer
    
    def get(self, request, *args, **kwargs):
        print(request.query_params.get('project',None))
        return self.list(request, *args, **kwargs)
    
    def get_queryset(self):
        queryset = ProjectDetails.objects.filter(project_reltn=self.request.query_params.get('project',None))
        print(queryset)
        return queryset