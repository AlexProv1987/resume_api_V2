from .models import Applicant
from rest_framework import serializers

class ApplicantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Applicant
        fields='__all__'