from rest_framework import serializers
from prikljucci.serializers import PrSer

from prikljucci.models import Prikljucak
from .models import Dokumenti


class DokumentSerializer(serializers.ModelSerializer):
    prikljucak = PrSer(required = False, allow_null=False, many = False)

    class Meta:
        model=Dokumenti
        fields=['id', 'zahtjev', 'zk_izvadak', 'katastarski_plan', 'prikljucak']

    def create(self, data):
        dokumenti= Dokumenti(
            zahtjev=data["zahtjev"],
            zk_izvadak=data["zk_izvadak"],
            katastarski_plan=data["katastarski_plan"],
            prikljucak=self.context["prikljucak"]

        )
        dokumenti.save()
        return dokumenti