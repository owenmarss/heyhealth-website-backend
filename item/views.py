from django.shortcuts import render
from rest_framework.request import Request
from rest_framework.decorators import api_view
from rest_framework.response import Response
from item.models import Item
from rest_framework import status
from .serializers import ItemSerializer
from rest_framework.views import APIView

# Create your views here.
class CreateListView(APIView):

    permission_classes = []

    # @api_view(['GET'])
    def get(self,request):
        allItems = list(Item.objects.all().values())
        return Response(data=allItems, status=status.HTTP_200_OK)

    # @api_view(['POST'])
    def post(self,request):
        serializer=ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)