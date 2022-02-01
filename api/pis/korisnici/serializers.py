from rest_framework import serializers

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



