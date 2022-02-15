from rest_framework import serializers
from tiket_statusi.serializers import TiketStatusSerializer
from .models import Tiket
from korisnici.serializers import UserSerializer
from korisnici.models import User 
from tiket_statusi.models import StatusTiketa

class TiketSerializer(serializers.ModelSerializer):
    korisnik= UserSerializer(required=False, allow_null=False, many=False)
    status = TiketStatusSerializer(required=False, allow_null=False, many=False)

    def create(self, validated_data):
        tiket=Tiket(
            naslov=validated_data["naslov"],
            opis_kvara=validated_data["opis_kvara"],
            korisnik= User.objects.get(pk=self.context["userID"]),
            status=StatusTiketa.objects.get(status="Aktivan")
        )
        tiket.save()
        return tiket

    class Meta:
        model=Tiket

        fields=['id' ,'naslov', 'opis_kvara', 'korisnik', 'status']



