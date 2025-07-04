from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from .serializers import *
from .models import *
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
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
    
class GetApplicantWorkData(APIView):
    def get(self, request, *args, **kwargs):
        return Response(WorkHistory.getWorkInformationSerialized(request.query_params.get('applicant',None)),status=HTTP_200_OK)