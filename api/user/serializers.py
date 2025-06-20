from .models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['password', 'last_login','is_active','is_staff','is_superuser','groups','date_joined','user_permissions',]