from .models import ApplicantFeedBack,LLMResponse
from rest_framework import serializers

class ApplicantFeedBackSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplicantFeedBack
        fields='__all__'
        
class LLMResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model=LLMResponse
        fields='__all__'