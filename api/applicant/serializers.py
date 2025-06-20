from .models import Applicant,ApplicantContactMethods,ApplicantSocials
from api.user.serializers import UserSerializer
from rest_framework import serializers
class ApplicantSerializer(serializers.ModelSerializer):
    user_reltn = UserSerializer()
    class Meta:
        model = Applicant
        fields='__all__'
        
class ApplicantContactSerializer(serializers.ModelSerializer):
    class Meta:
        model=ApplicantContactMethods
        fields='__all__'
        
class ApplicantSocialsSerializer(serializers.ModelSerializer):
    class Meta:
        model=ApplicantSocials
        fields='__all__'
        
class GetApplicantSetSerializer(serializers.ModelSerializer):
    user_reltn = UserSerializer()
    contact_method = ApplicantContactSerializer(many=True,read_only=True)
    social = ApplicantSocialsSerializer(many=True, read_only=True)
    class Meta:
        model=Applicant
        fields='__all__'