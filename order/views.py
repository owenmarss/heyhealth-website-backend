from django.shortcuts import render
from rest_framework.request import Request
from rest_framework.decorators import api_view
from rest_framework.response import Response
from order.models import Order
from rest_framework import status
from .serializers import OrderResponseSerializer, OrderSerializer
from rest_framework.views import APIView

# Create your views here.
class CreateListView(APIView):
    
    # @api_view(['GET'])
    def get(self,request):
        allOrders = list(Order.objects.all())
        serializer = OrderResponseSerializer(allOrders, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    # @api_view(['POST'])
    def post(self,request):
        serializer=OrderSerializer(data=request.data, context={'request':request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class GetMyOrderView(APIView):
    
    # @api_view(['GET'])
    def get(self,request):
        allOrders = list(Order.objects.filter(user=request.user))
        serializer = OrderResponseSerializer(allOrders, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)