from urllib import response
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from dokumenti_ugovora.serializers import DokumentSerializer
from .models import Dokumenti
from prikljucci.models import Prikljucak
from prikljucak_statusi.models import StatusPrikljucka
from rest_framework.parsers import MultiPartParser, FormParser
from ulice.models import Ulica
from prikljucak_statusi.models import StatusPrikljucka


class ZahtjeviView(APIView):
    permission_classes=(IsAuthenticated,)
    parser_classes=(MultiPartParser, FormParser)

    def post(self, request):
        zdata={}
        print(1)
        print(request.data)
        try:
            prikljucak=Prikljucak(
                korisnik=request.user,
                ulica=Ulica.objects.get(ulica=request.data["ulica"]),
                kucni_broj=request.data["kucni_broj"],
                status=StatusPrikljucka.objects.get(status="Zahtjev")

            )
            prikljucak.save()
            
            zdata["zahtjev"]=request.data["zahtjev"]
            zdata["zk_izvadak"]=request.data["zk_izvadak"]
            zdata["katastarski_plan"]=request.data["katastarski_plan"]
            ctx={"prikljucak":prikljucak}
            serializer=DokumentSerializer(data=zdata, context=ctx)
            if serializer.is_valid():
                serializer.save()
                return Response({"message":"succes"}, status=status.HTTP_201_CREATED)
            print(serializer.errors)
            print(2)
            return Response({"error":serializer.errors},status=status.HTTP_400_BAD_REQUEST )
        except Exception as e:
            print(str(e))
            print(3)
            return Response({"error":str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        if request.user.rola.rola!="Administrator":
            return Response({"message":"Unauthorized"}, status=status.HTTP_401_UNAUTHORIZED)
        
        if Dokumenti.objects.filter(prikljucak__status__status="Zahtjev").exists():
            zahtjevi=Dokumenti.objects.filter(prikljucak__status__status="Zahtjev").order_by("-id")
            serializer=DokumentSerializer(zahtjevi, many=True)
            return Response(data={"zahtjevi":serializer.data}, status=status.HTTP_200_OK)
                
        else:
            return Response({"message":"Nema zahtjeva"}, status=status.HTTP_404_NOT_FOUND)

     
class ZahtjevDetailsView(APIView):
    permission_classes=(IsAuthenticated,)
    
    def get_obj(self, id):
        try:
            return Dokumenti.objects.get(id=id)
        except Dokumenti.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    def get_status(self, st):
        try:
            return StatusPrikljucka.objects.get(status=st)
        except StatusPrikljucka.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


    def get(self,request, id):
        if request.user.rola.rola!="Administrator":
            return Response({"message":"Unauthorized"}, status=status.HTTP_401_UNAUTHORIZED)
        
        zahtjevi=self.get_obj(id)
        if zahtjevi.prikljucak.status.status!="Zahtjev":
            return Response({"message":"Zahtjev je već obrađen"}, status=status.HTTP_409_CONFLICT)
        serializer=DokumentSerializer(zahtjevi)
            
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, id):
        if request.user.rola.rola!="Administrator":
            return Response({"message":"Unauthorized"}, status=status.HTTP_401_UNAUTHORIZED)
        st=self.get_status("Aktivan")
        zahtjev=self.get_obj(id)
        prikljucak=zahtjev.prikljucak
        prikljucak.status=st
        prikljucak.save()
        return Response({"message":"Succes"},status=status.HTTP_202_ACCEPTED)
        

            
    


