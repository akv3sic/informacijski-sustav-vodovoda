
from multiprocessing import context
from tkinter import EXCEPTION
from .models import Tiket, StatusTiketa
from tiket_statusi.serializers import TiketStatusSerializer
from korisnici.serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .serializers import TiketSerializer
from rest_framework.response import Response
from rest_framework import status

class KvarView(APIView):
    permission_classes=(IsAuthenticated,)

    def post(self, request):
        
       
        data={
            
            "naslov":request.data["naslov"],
            "opis_kvara":request.data["opis_kvara"]
                }

       
        serializer = TiketSerializer(data=data, context={"userID":request.user.id})
        if serializer.is_valid():
            serializer.save()
            return Response(data={"message":"Succes"}, status=status.HTTP_201_CREATED)
        else :
            return Response(serializer.errors)
    
class Kvar(APIView):
    permission_classes=(IsAuthenticated,)

    def get(self, request):
        try:
            
            if request.user.rola.rola=="Administrator":
                print(request.query_params.get("id"))
                if request.query_params.get("id")==None:
                    st=Tiket.objects.all()
                elif request.query_params.get("id")=="1":
                    st=Tiket.objects.filter(status__status="Aktivan")
                elif request.query_params.get("id")=="2":
                    st=Tiket.objects.filter(status__status="Riješen")

                else:
                    return Response({"message":"Bad Request"}, status=status.HTTP_400_BAD_REQUEST)
                
                serializer=TiketSerializer(st, many=True)
                return Response(data=serializer.data)
            else:
                return Response({"message":"Unauthorized"}, status=status.HTTP_401_UNAUTHORIZED)
            
        except Exception as e:
            return Response({"message":str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

    def put(self,request):
        print(request.data["id"])
        try:
            if request.user.rola.rola=="Administrator":
                
                if  not Tiket.objects.get(id=request.data["id"]):
                    return Response({"message":"Bad request"}, status=status.HTTP_400_BAD_REQUEST)
                tiket=Tiket.objects.get(id=request.data["id"])
                tiket.status=StatusTiketa.objects.get(status="Riješen")
                tiket.save()
                return Response({"message":"Successful"}, status=status.HTTP_202_ACCEPTED)
            else:
                return Response({"message":"Unauthorized"}, status=status.HTTP_401_UNAUTHORIZED)
        except Exception as e:
            return Response({"message":str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
                
