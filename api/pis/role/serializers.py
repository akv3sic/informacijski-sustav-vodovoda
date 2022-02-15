from rest_framework import serializers
from .models import Rola

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model=Rola
        fields=['rola']