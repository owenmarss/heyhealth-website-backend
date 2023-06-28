from django.shortcuts import render
from rest_framework.request import Request
from rest_framework.decorators import api_view
from rest_framework.response import Response
from janji.models import Janji
from rest_framework import status
from rest_framework.views import APIView
from janji.serializers import JanjiResponseSerializer, JanjiSerializer

# Create your views here.
class CreateListView(APIView):

    # @api_view(['GET'])
    def get(self,request):
        allJanji = list(Janji.objects.all())
        serializer = JanjiResponseSerializer(allJanji, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    # @api_view(['POST'])
    def post(self,request):
        serializer=JanjiSerializer(data=request.data, context={'request':request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class GetMyJanjiView(APIView):

    # @api_view(['GET'])
    def get(self,request):
        allJanji = list(Janji.objects.filter(user=request.user))
        serializer = JanjiResponseSerializer(allJanji, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)