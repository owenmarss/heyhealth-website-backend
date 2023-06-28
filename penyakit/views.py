from django.shortcuts import render
from rest_framework.request import Request
from rest_framework.decorators import api_view
from rest_framework.response import Response
from penyakit.models import Penyakit
from rest_framework import status
from .serializers import PenyakitSerializer
from rest_framework.views import APIView

# Create your views here.
class CreateListView(APIView):

    permission_classes = []

    # @api_view(['GET'])
    def get(self,request):
        allPenyakit = list(Penyakit.objects.all().values())
        return Response(data=allPenyakit, status=status.HTTP_200_OK)

    # @api_view(['POST'])
    def post(self,request):
        serializer=PenyakitSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)