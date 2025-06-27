from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from django.shortcuts import get_object_or_404
from .models import ApplicantFeedBack
from .serializers import LLMResponseSerializer
from api.applicant.models import Applicant
from datetime import timedelta
from django.utils import timezone
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

class CreateFeedBack(APIView):
    
    def post(self, request, *args, **kwargs):
        return self.handle_rating(request, *args, **kwargs)
    
    def has_recent_rating(self,ip, hours=1):
        now = timezone.now()
        time_threshold = now - timedelta(hours=hours)

        return ApplicantFeedBack.objects.filter(
            ip_address=ip,
            created_at__gte=time_threshold
        ).exists()

    def has_rated_item(self,ip, applicant):
        return ApplicantFeedBack.objects.filter(
            ip_address=ip,
            applicant_reltn=applicant
        ).exists()
        
    def get_client_ip(self,request):
        x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0].strip()
        else:
            ip = request.META.get("REMOTE_ADDR")
        return ip
    
    def handle_rating(self,request):
        applicant = get_object_or_404(Applicant, id=request.data.get('applicant_reltn',None))
        ip = self.get_client_ip(request)

        if self.has_rated_item(ip, applicant):
            return Response({"error": f"You already provided feedback for {applicant.user_reltn.first_name} {applicant.user_reltn.last_name}."}, status=status.HTTP_400_BAD_REQUEST)
        
        if self.has_recent_rating(ip):
            return Response({"error": "You are rating too frequently. Please wait."}, status=status.HTTP_429_TOO_MANY_REQUESTS)
        
        
        ApplicantFeedBack.objects.create(
            applicant_reltn=applicant,
            rating=request.data.get("rating"),
            ip_address=ip,
            user_agent=request.META.get("HTTP_USER_AGENT", ""),
            comment=request.data.get("comment",None)
        )
        
        return Response({"success": True}, status=status.HTTP_201_CREATED)
    
class StoreLLMResponse(CreateAPIView):
    serializer_class=LLMResponseSerializer
    