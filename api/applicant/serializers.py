from .models import Applicant
from api.user.serializers import UserSerializer
from rest_framework import serializers

class ApplicantSerializer(serializers.ModelSerializer):
    user_reltn = UserSerializer()
    class Meta:
        model = Applicant
        fields='__all__'