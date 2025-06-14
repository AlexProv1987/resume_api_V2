from .models import *
from rest_framework import serializers

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields=('skill_name','skill_description','years_of_experience',)

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