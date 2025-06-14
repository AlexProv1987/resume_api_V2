from rest_framework.generics import ListAPIView
from .serializers import *
from .models import *
# Create your views here.
class GetApplicantWorkHistory(ListAPIView):
    
    serializer_class=WorkHistorySerializer
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def get_queryset(self):
        queryset = WorkHistory.objects.filter(applicant_reltn=self.request.query_params.get('applicant',None))
        return queryset

class GetWorkHistoryDetails(ListAPIView):
    
    serializer_class=WorkHistoryDetailsSerializer
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def get_queryset(self):
        queryset = WorkHistoryDetails.objects.filter(work_reltn=self.request.query_params.get('work_id',None))
        return queryset