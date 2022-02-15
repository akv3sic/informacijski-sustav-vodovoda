from rest_framework import serializers
from .models import Racun

class RacunSerializer(serializers.ModelSerializer):
    prikljucakID=serializers.IntegerField(source="prikljucak.id")
    class Meta:
        model=Racun

        fields=[
                'id',
                'prikljucakID', 
                'mjesec', 
                'datum_placanja', 
                'datum_dospijeca', 
                'placeno',
                'ukupno',
                'dug', 
                'iznos'

                
                ]

class PotrosnjaSerializer(serializers.ModelSerializer):
    datum_ocitavanja=serializers.DateField(source="date_created")

    class Meta:
        model = Racun

        fields=[
            'datum_ocitavanja',
            'mjesec',
            'prethodno_stanje',
            'brojilo',
            'potrosnja'

        ]