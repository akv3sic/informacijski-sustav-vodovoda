from django.forms import ValidationError
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import Cjenovnik
from rest_framework.views import APIView
from .serializers import CjenovnikSerializer

class CjenovnikView(APIView):

    permission_classes=(IsAuthenticated,)

    def get(self, request):
        serializer=CjenovnikSerializer(Cjenovnik.objects.latest('date_created'))
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        try:
            data={}
            data["kategorija1_cijena"]=request.data["kategorija1_cijena"]
            data["kategorija2_cijena"]=request.data["kategorija2_cijena"]
            data["kategorija3_cijena"]=request.data["kategorija3_cijena"]
            data["kategorija1_granica"]=request.data["kategorija1_granica"]
            data["kategorija2_granica"]=request.data["kategorija2_granica"]

            serializer=CjenovnikSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(data=serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            raise ValidationError({"400":f'{str(e)}'})  




