from .models import *
from rest_framework import serializers

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields='__all__'

class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields='__all__'
        
class CertificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certification
        fields='__all__'
        
class ReferencesSerializer(serializers.ModelSerializer):
    class Meta:
        model = References
        fields='__all__'
        
class AdditionalContextSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdditionalContext
        fields='__all__'