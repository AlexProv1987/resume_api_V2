from rest_framework.generics import RetrieveAPIView
from .serializers import ApplicantSerializer
from .models import Applicant
from io import BytesIO
from reportlab.pdfgen import canvas
from rest_framework.views import APIView
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from api.work_details.models import WorkHistory,WorkHistoryDetails
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
        self._getWorkInformation(applicant)
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
    
    def _getWorkInformation(self,applicant:Applicant):
        work_queryset = WorkHistory.objects.filter(applicant_reltn=applicant).prefetch_related('work_details')
        work_list = []
        for work in work_queryset:
            work_details = list(work.work_details.all())  # or work.details.all() if using related_name='details'
            work_list.append({
                "work": work,
                "details": work_details
            })
        print(work_list)
        #work_history = WorkHistoryDetails.objects.filter(work_reltn=work)
        
    def _getProjectInformation(self):
        pass
    
    def _getImageFromUrl(self,url):
        response = requests.get(url)
        if response.status_code == 200:
            return BytesIO(response.content)
        return None