from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from .serializers import *
from .models import *

@api_view(('GET',))
def home(request):
    return Response(data={"test":"data"})

@api_view(('POST',))
def addCustomer(request):
    serializer = CustomerSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(('GET',))
def getCustomers(request):
    try:
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response(data={"error":str(e)}, status=status.HTTP_400_BAD_REQUEST)

@api_view(('POST',))
def addOrder(request):
    serializer = OrderSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(('GET',))
def getOrders(request):
    try:
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response(data={"error":str(e)}, status=status.HTTP_400_BAD_REQUEST)

@api_view(('POST',))
def addItem(request):
    serializer = ItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(('GET',))
def getOrderByID(request,pk):
    try:
        order = Order.objects.get(pk=pk)
        serializer = OrderSerializer(order)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response(data={"error":str(e)}, status=status.HTTP_400_BAD_REQUEST)

@api_view(('PUT',))
def updateItem(request,pk):
    try:
        item = Item.objects.get(pk=pk)
    except:
        return Response({"error":"Item does not exist"}, status=status.HTTP_404_NOT_FOUND)
    serializer = ItemSerializer(item, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)