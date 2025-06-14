from rest_framework.generics import RetrieveAPIView
from .serializers import ApplicantSerializer
from .models import Applicant
# Create your views here.
class GetApplicant(RetrieveAPIView):
    queryset=Applicant.objects.all()
    serializer_class=ApplicantSerializer