from .models import StatusTiketa
from rest_framework import serializers


class TiketStatusSerializer(serializers.ModelSerializer):

    
    class Meta:
        model=StatusTiketa
        fields=["status"]