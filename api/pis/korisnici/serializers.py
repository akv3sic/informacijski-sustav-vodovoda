from rest_framework import serializers
from ulice.models import Ulica
from role.models import Rola
from .models import User




class RegistrationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields= [
            "email",
            "username",
            "userlastname",
            "password",
            #"rola"
        ]

        extra_kwargs = {"password": {"write_only": True}}
        
        def create(self, validated_data):
            user=User(
                email=validated_data['email'],
                username=validated_data['username'],
                userlastname=validated_data['userlastname']
            )
            user.set_password(validated_data['password'])
            #if validated_data["rola"]!=None:
             #   user.rola=validated_data["rola"]
            user.save()
            return user



class UserDataSerializer(serializers.ModelSerializer):
    ulica=serializers.CharField(source="ulica.ulica")
    def update(self, instance, validated_data):
                
        instance.username = validated_data.get('username', instance.username)
        instance.userlastname = validated_data.get('userlastname', instance.userlastname)
        instance.telefon=validated_data.get('telefon', instance.telefon)
        instance.ulica=Ulica.objects.get(ulica=validated_data['ulica']['ulica'])
        
        instance.kucni_broj=validated_data.get('kucni_broj', instance.kucni_broj)
        instance.save()
        return instance
    class Meta:
        model=User
        
        fields=['email', 'username', 'userlastname', 'telefon', 'ulica', 'kucni_broj']

