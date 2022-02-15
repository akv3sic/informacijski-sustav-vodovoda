from rest_framework import serializers

from korisnici.serializers import UserListSerializer


from .models import Prikljucak

class PrikljucakSerializer(serializers.ModelSerializer):
    ulica=serializers.CharField(source="ulica.ulica")
    mjesto=serializers.CharField(source="ulica.mjesto.mjesto")
    class Meta:
        model=Prikljucak

        fields=[ 'id','ulica', 'kucni_broj', 'mjesto']

class PrSer(serializers.ModelSerializer):
    ulica=serializers.CharField(source="ulica.ulica")
    mjesto=serializers.CharField(source="ulica.mjesto.mjesto")
    korisnik=UserListSerializer(required=False, allow_null=False, many=False)
    class Meta:
        model=Prikljucak

        fields=[ 'id','ulica', 'kucni_broj', 'mjesto', 'korisnik']
        