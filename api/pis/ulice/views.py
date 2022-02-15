from rest_framework.response import Response
from rest_framework import status
from .models import Ulica
from .serializers import UlicaSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from mjesta.models import Mjesto


class UliceView(APIView):
    permission_classes=(IsAuthenticated,)

    def get(self,request):
        if (not request.query_params.get("mjesto")) and (not Mjesto.objects.get(mjesto=request.query_params.get("mjesto"))):
            return Response({"message":"Bad request"}, status=status.HTTP_400_BAD_REQUEST)
        ulice=Ulica.objects.filter(mjesto=Mjesto.objects.get(mjesto=request.query_params.get("mjesto")))
        serializer= UlicaSerializer(ulice, many=True)
        return Response(serializer.data)