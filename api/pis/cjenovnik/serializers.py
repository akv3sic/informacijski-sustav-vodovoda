from rest_framework import serializers
from .models import Cjenovnik

class CjenovnikSerializer(serializers.ModelSerializer):
    class Meta:
        model=Cjenovnik
        fields='__all__'