from django.shortcuts import render
from rest_framework.request import Request
from rest_framework.decorators import api_view
from rest_framework.response import Response
from dokter.models import Dokter
from rest_framework import status
from .serializers import DokterSerializer
from rest_framework.views import APIView

# Create your views here.
class CreateListView(APIView):

    permission_classes = []

    # @api_view(['GET'])
    def get(self,request):
        allDokter = list(Dokter.objects.all())
        serializer = DokterSerializer(allDokter, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    # @api_view(['POST'])
    def post(self,request):
        serializer=DokterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)