import json
from ulice.models import Ulica
from ulice.serializers import UlicaSerializer
from rest_framework.views import APIView
from django.contrib.auth import login, logout
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from .models import User
from .serializers import RegistrationSerializer, UserDataSerializer, UserListSerializer
from role.models import Rola
from django.db.models import Q


@api_view(["POST"])
@permission_classes([AllowAny | IsAuthenticated])
def registerUsers(request):
    try:
        print(request.user)
        data={}
        reqdata={
            "email":request.data["email"],
            "username":request.data["username"],
            "userlastname":request.data["userlastname"],
            "password":request.data["password"]
        }
        
        serializer=RegistrationSerializer(data=reqdata)
        if serializer.is_valid():
            user = serializer.save()
            user.is_active=True
            if (request.user.id == None) and (request.data["rola"]!=None):
                user.delete()
                return Response({"message":"Bad request"}, status=status.HTTP_400_BAD_REQUEST) 

            if request.user.id != None:
                if request.user.rola==Rola.objects.get(rola="Administrator"):
                    user.rola=Rola.objects.get(rola=request.data["rola"])
                else:
                    user.delete()
                    return Response(data={"message":"Nemate permisije!!"}, status=status.HTTP_403_FORBIDDEN)
            else:
                user.rola=Rola.objects.get(rola="Korisnik")        
            user.save()
            token = Token.objects.get_or_create(user=user)[0].key
            data["token"]=token
            data["message"]="Uspješna registracija"
            data['username']=user.username
            data['userlastname']=user.userlastname
            data["rola"]=user.rola.rola
            return Response(data=data, status=status.HTTP_201_CREATED)
        else:
            
            data = serializer.errors
            print(data)
            return Response(data)
    
    except Exception as e:
        
        raise ValidationError({"400":f'{str(e)}'})


@api_view(["POST"])   
@permission_classes([AllowAny])
def loginUsers(request):

    
    reqBody= json.loads(request.body) 
    email=reqBody['email']    
    password = reqBody['password']

    try:
        user = User.objects.get(email=email)
    except BaseException as e:
        raise ValidationError ({"400": f'{str(e)}'})

    token = Token.objects.get_or_create(user=user)[0].key
    if not user.check_password(password):
        print("1")
        raise ValidationError({'message': 'Pogrešan mail ili lozinka'})

    if user:
        if user.is_active:
            login(request, user)
            msg= "Uspješna prijava"
            response = {'username':user.username, "userlastname":user.userlastname, 'message': msg, 'token':token, 'rola':user.rola.rola}
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

class UserUpdate(APIView):
    permission_classes=(IsAuthenticated,)
    

    def get(self, request):
        user = request.user
        serializer= UserDataSerializer(user)
        serializer2=UlicaSerializer(Ulica.objects.all(), many= True)
        data={}
        data['korisnik']=serializer.data
        data['ulice']=serializer2.data
        return Response(data=data, status=status.HTTP_200_OK)

    def put(self, request):
        user = request.user
        print(request.data)
        serializer = UserDataSerializer(user, data= request.data)
        serializer2=UlicaSerializer(Ulica.objects.all(), many= True)
        data={}
        if serializer.is_valid():
            serializer.save()
            data['korisnik']=serializer.data
            data['ulice']=serializer2.data
            return Response(data=data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserList(APIView):

    permission_classes=(IsAuthenticated,)

    def get(self, request):
        rola=int(request.query_params.get("rola"))
        if rola==1:
            userList= User.objects.all().filter(rola__rola="Korisnik")
        elif rola==2:
            userList= User.objects.all().filter(Q(rola__rola="Administrator") | Q(rola__rola="Popisivač")).order_by('id')
        else:
            return Response({"message":"Bad request"}, status=status.HTTP_400_BAD_REQUEST)
        serializer=UserListSerializer(userList, many=True)
        return Response(serializer.data)
    
    
