from datetime import datetime, date
from cjenovnik.models import Cjenovnik
from prikljucci.models import Prikljucak
from .models import Racun
from .serializers import RacunSerializer, PotrosnjaSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
def get_graf_data(potrosnja):
    spliter= (potrosnja[0].mjesec).split("/")
    i=int(spliter[0])
    graf={
        "labels":[],
        "potrosnja":[]
    }

    

    for racun in potrosnja :
        graf["labels"].insert(0, i)
        graf["potrosnja"].insert(0, racun.potrosnja)
        if i==1:
            i=12
        else:
            i=i-1
    
    while i != int(spliter[0]):
        graf["labels"].insert(0,i),
        graf["potrosnja"].insert(0, 0)
        if i==1:
            i=12
        else:
            i=i-1
        

    return graf



def get_mjesec():
    dat= datetime.now()
    if dat.month >1:
        mjesec= dat.month -1
        god=dat.year
    else:
        mjesec=12
        god=dat.year-1
    if mjesec<10:
        mjesec="0"+str(mjesec)
    res=mjesec+"/"+str(god)
    print(res)
    return res

def izracun_cijene(potrosnja, cjenovnik):
    iznos=0
    if potrosnja>int(cjenovnik.kategorija2_granica):
        iznos=iznos +((potrosnja-cjenovnik.kategorija2_granica)*cjenovnik.kategorija3_cijena)
        potrosnja=cjenovnik.kategorija2_granica
    
    if potrosnja>int(cjenovnik.kategorija1_granica):
        iznos=iznos +((potrosnja-cjenovnik.kategorija1_granica)*cjenovnik.kategorija2_cijena)
        potrosnja=cjenovnik.kategorija1_granica

    iznos = iznos + (potrosnja * cjenovnik.kategorija1_cijena)
    return iznos

class RacuniView(APIView):
    permission_classes=(IsAuthenticated,)

    def get(self, request):
       
        idPrikljucka=request.query_params.get("idPrikljucka")
        racuni= Racun.objects.filter(prikljucak__id = idPrikljucka, on_hold=False ).order_by("-id")
        serializer=RacunSerializer(racuni, many=True)
        data={}
        
        data["racuni"]=serializer.data
        return Response(data=data, status=status.HTTP_200_OK)


class PotrosnjaView(APIView):
    permission_classes=(IsAuthenticated,)

    def get(self, request):
        try:

            idPrikljucka = request.query_params.get("idPrikljucka")
            if Prikljucak.objects.get(id=idPrikljucka):
                
                priklj= Prikljucak.objects.get(id=idPrikljucka)
                if priklj.korisnik != request.user:
                    return Response({"message":"Unauthorized!"}, status=status.HTTP_401_UNAUTHORIZED)
                if not(Racun.objects.filter(prikljucak__id = idPrikljucka, on_hold=False).exists()):
                    return Response({"potrosnja":[]}, status=status.HTTP_200_OK)
                
                potrosnja= Racun.objects.filter(prikljucak__id = idPrikljucka, on_hold=False).order_by('-id')[:12]
                graf= get_graf_data(potrosnja)

                
                serializer = PotrosnjaSerializer(potrosnja, many=True)
                
                



                data={}
                data['potrosnja']=serializer.data
                data["graf"]=graf
                return Response(data=data, status=status.HTTP_200_OK)
            else: 
                return Response({"message":"Bad request"}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error":str(e)}, status=status.HTTP_404_NOT_FOUND)

class PopisPrikljucaka(APIView):
    permission_classes=(IsAuthenticated,)
    
    def get(self, request):
        data={"prikljucci":[]}
        if request.user.rola.rola!="Administrator":
            if request.user.rola.rola!="Popisivač":
                return Response({"message":"Unauthorized"}, status=status.HTTP_401_UNAUTHORIZED)
        if request.user.rola.rola=="Administrator":
            if Prikljucak.objects.filter(status__status="Zahtjev").exists:
                broj_zahtjeva= Prikljucak.objects.filter(status__status="Zahtjev").count()
                
            else:
                broj_zahtjeva=0
            
            data["broj_zahtjeva"]=broj_zahtjeva
        ulica=request.query_params.get("ulica")
        mjesto=request.query_params.get("mjesto")
        blacklist=[]
        
        if ulica != None:
            racuni=Racun.objects.filter(prikljucak__ulica__ulica=ulica, prikljucak__status__status="Aktivan").order_by('-date_created')
            prikljucci= Prikljucak.objects.filter(ulica__ulica=ulica, status__status="Aktivan")
        elif mjesto != None:
            racuni=Racun.objects.filter(prikljucak__ulica__mjesto__mjesto=mjesto, prikljucak__status__status="Aktivan").order_by('-date_created')
            prikljucci= Prikljucak.objects.filter(ulica__mjesto__mjesto=mjesto, status__status="Aktivan")

        else:
            racuni=Racun.objects.filter(prikljucak__status__status="Aktivan").order_by('-date_created')
            prikljucci= Prikljucak.objects.filter(status__status="Aktivan")
        
        for racun in racuni:
            if racun.prikljucak in blacklist:
                pass
            else:
                blacklist.append(racun.prikljucak)
                if (racun.date_created.month==datetime.now().month) and (racun.date_created.year==datetime.now().year):
                    popisan=True
                else:
                    popisan=False
                r={
                    "idPrikljucka":racun.prikljucak.id,
                    "username":racun.prikljucak.korisnik.username,
                    "userlastname":racun.prikljucak.korisnik.userlastname,
                    "mjesto":racun.prikljucak.get_mjesto,
                    "ulica":racun.prikljucak.get_ulica,
                    "kucni_broj":racun.prikljucak.kucni_broj,
                    "stanje_brojila":racun.brojilo,
                    "popisan":popisan
                }
                data["prikljucci"].append(r)
        for prikljucak in prikljucci:
            if prikljucak in blacklist:
                pass
            else:
                blacklist.append(prikljucak)
                r={
                    "idPrikljucka":prikljucak.id,
                    "username":prikljucak.korisnik.username,
                    "userlastname":prikljucak.korisnik.userlastname,
                    "mjesto":prikljucak.get_mjesto,
                    "ulica":prikljucak.get_ulica,
                    "kucni_broj":prikljucak.kucni_broj,
                    "stanje_brojila":0,
                    "popisan":False
                }
                data["prikljucci"].append(r)



        return Response(data=data, status=status.HTTP_200_OK)

class StanjeBrojilaView(APIView):
    permission_classes=(IsAuthenticated,)

    def post(self, request):
        if request.user.rola.rola!="Popisivač":
            return Response({"message":"Unauthorized"}, status=status.HTTP_401_UNAUTHORIZED)

        try:
            cjenovnik= Cjenovnik.objects.last()
            priklj=Prikljucak.objects.get(id=request.data["idPrikljucka"])
            stBr=request.data["stanjeBrojila"]
            stBr=int(stBr)
            if Racun.objects.filter(prikljucak=priklj).exists():
                zadnjirac=Racun.objects.filter(prikljucak=priklj).last()
                if (zadnjirac.date_created.month == datetime.now().month) and (zadnjirac.date_created.year==datetime.now().year):
                    return Response({"message":"Već popisano"}, status=status.HTTP_400_BAD_REQUEST)
                if int(zadnjirac.brojilo) > int(stBr):
                    return Response({"message":"Neispravan unos"}, status=status.HTTP_400_BAD_REQUEST)
                if zadnjirac.placeno==False:
                    dug=zadnjirac.iznos + zadnjirac.dug
                
                else:
                    dug=0
                potrosnja=stBr - zadnjirac.brojilo

            else:
                potrosnja=stBr
                dug=0
            iznos=izracun_cijene(potrosnja, cjenovnik)
            
            
            popisivac=request.user
            mjesec=get_mjesec()

            racun=Racun(
                brojilo=stBr,
                prikljucak=priklj,
                potrosnja=potrosnja,
                iznos=iznos,
                dug=dug,
                popisivac=popisivac,
                cjenovnik=cjenovnik,
                mjesec=mjesec
                )
            racun.save()
            return Response({"message":"Succes"}, status=status.HTTP_201_CREATED)
        except Exception as e:
            print(str(e))
            return Response({"message":str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request):
        if request.user.rola.rola!="Administrator":
            return Response({"message":"Unauthorized"}, status=status.HTTP_401_UNAUTHORIZED)
        
        try:
            if Racun.objects.filter(on_hold=True).exists():
                racuni=Racun.objects.filter(on_hold=True)
                racuni.update(on_hold=False, datum_dospijeca=date.today())
            return Response({"message":"Succes"}, status=status.HTTP_202_ACCEPTED)
        except Exception as e:
            return Response({"message":str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



@api_view(["get"])
@permission_classes([IsAuthenticated])
def broj_racuna(request):
    if request.user.rola.rola!="Administrator":
        return Response({"message":"Unauthorized"}, status=status.HTTP_401_UNAUTHORIZED)
    if Racun.objects.filter(on_hold=True).exists():
        br=Racun.objects.filter(on_hold=True).count()
        data={"broj_racuna":br}
    else:
        data={"broj_racuna":0}
    return Response(data=data, status=status.HTTP_200_OK)

