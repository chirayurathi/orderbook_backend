from .models import *
from rest_framework import serializers

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class ItemSerializer(serializers.ModelSerializer):
    order_id = serializers.PrimaryKeyRelatedField(source='order', queryset=Order.objects.all())
    class Meta:
        model = Item
        fields = '__all__'
        read_only_fields=['order']

class OrderSerializer(serializers.ModelSerializer):
    customer_id = serializers.PrimaryKeyRelatedField(source='customer',queryset=Customer.objects.all(), write_only=True)
    customer = CustomerSerializer(read_only=True)
    items = ItemSerializer(many=True, read_only=True)
    class Meta:
        model = Order
        fields = ['id','amount','customer','items','customer_id','created_at','due_date']
        read_only_fields = ['id','items','customer','created_at']
