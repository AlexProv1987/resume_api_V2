from rest_framework.generics import RetrieveAPIView
from .serializers import ApplicantSerializer
from .models import Applicant
from io import BytesIO
from reportlab.pdfgen import canvas
from rest_framework.views import APIView
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from api.work_details.models import WorkHistory
import requests
# Create your views here.
class GetApplicant(RetrieveAPIView):
    queryset=Applicant.objects.all()
    serializer_class=ApplicantSerializer
    
class GetResume(APIView):
    
    def get(self,request,pk):
        
        return self.generate_pdf(request,pk)
        
    def generate_pdf(self,request,pk):
        
        applicant = get_object_or_404(Applicant,id=pk)
        work_hist = WorkHistory.getWorkInformationObj(applicant)
        buffer = BytesIO()
        p = canvas.Canvas(buffer)
        p.drawString(100, 750, "Hello from Django PDF!")
        p.showPage()
        p.save()

        buffer.seek(0)
        
        return HttpResponse(
            buffer,
            content_type='application/pdf',
            headers={
                'Content-Disposition': 'inline; filename="generated.pdf"',
            },
        )
    
    def _getCertifications(self):
        pass
    
    def _getSkill(self):
        pass
    
    def _getEducation(self):
        pass
    
    def _getReferences(self):
        pass
        
    def _getProjectInformation(self):
        pass
    
    def _getImageFromUrl(self,url):
        response = requests.get(url)
        if response.status_code == 200:
            return BytesIO(response.content)
        return None