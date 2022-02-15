from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Mjesto
from .serializers import MjestoSerializer
from rest_framework.permissions import IsAuthenticated

class MjestaView(APIView):

    permission_classes=(IsAuthenticated,)

    def get(self, request):
        mjesta=Mjesto.objects.all()
        serializer=MjestoSerializer(mjesta, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
        
