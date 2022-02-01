import json
from django.contrib.auth import login, logout
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from .models import User
from .serializers import RegistrationSerializer


@api_view(["POST"])
@permission_classes([AllowAny])
def registerUsers(request):
    try:
        data={}
        serializer=RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            user.is_active=True
            user.save()
            token = Token.objects.get_or_create(user=user)[0].key
            data["token"]=token
            data["message"]="Uspješna registracija"
            return Response(data=data, status=status.HTTP_201_CREATED)
        else:
            data = serializer.errors
            return Response(data)
    
    except Exception as e:
        raise ValidationError({"400":f'{str(e)}'})


@api_view(["POST"])   
@permission_classes([AllowAny])
def loginUsers(request):

    data={}
    reqBody= json.loads(request.body) 
    email=reqBody['email']    
    password = reqBody['password']

    try:
        user = User.objects.get(email=email)
    except BaseException as e:
        raise ValidationError ({"400": f'{str(e)}'})

    token = Token.objects.get_or_create(user=user)[0].key
    if user.check_password(password):
        print("1")
        raise ValidationError({'message': 'Pogrešan mail ili lozinka'})

    if user:
        if user.is_active:
            login(request, user)
            data['message']= "Uspješna prijava"
            response = { 'data': data, 'token':token}
            print("2")

            return Response(data=response, status = status.HTTP_200_OK )
        else: 
            print("3")
            raise ValidationError({'400': f'Korisnički račun nije aktivan'})
    else:
        print("4")
        raise ValidationError({"400": f'Korisnički račun ne postoji'})


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def userLogout(request):
    request.user.auth_token.delete()

    logout(request)

    return Response('Uspješna odjava')