from .models import ApplicantFeedBack
from rest_framework import serializers

class ApplicantFeedBackSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplicantFeedBack
        fields='__all__'