from .models import *
from rest_framework import serializers

class WorkHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkHistory
        fields='__all__'

class WorkHistoryDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkHistoryDetails
        fields='__all__'
  