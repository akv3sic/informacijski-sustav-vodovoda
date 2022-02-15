from rest_framework import serializers
from .models import Mjesto


class MjestoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Mjesto
        fields='__all__'