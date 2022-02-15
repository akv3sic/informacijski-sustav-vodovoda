from .models import Prikljucak
from .serializers import PrikljucakSerializer
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status


class PrikljucakView(APIView):
    permission_classes=(IsAuthenticated,)

    def get(self, request):
        user= request.user
        print(user.id)
        prikljucci= Prikljucak.objects.filter(korisnik=user, status__status="Aktivan")
        print(prikljucci)
        serializer=PrikljucakSerializer(prikljucci, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK )
