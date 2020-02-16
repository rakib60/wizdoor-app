from rest_framework import serializers

from accounts.models import Customer
from product.serializers import ProductSerializer

from .models import Order, OrderItem


class CustomerMinifiedSerializer(serializers.ModelSerializer):
    customer_name = serializers.ReadOnlyField(
        source='name',
        read_only=True
    )

    class Meta:
        model =Customer
        fields = ('customer_name', 'location', 'phone')


class OrderItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    total_item_price = serializers.ReadOnlyField(
        source='get_total_item_price',
        read_only=True
    )

    total_discount_item_price = serializers.ReadOnlyField(
        source='get_total_discount_item_price',
        read_only=True
    )

    amount_saved = serializers.ReadOnlyField(
        source='get_amount_saved',
        read_only=True
    )

    final_price = serializers.ReadOnlyField(
        source='get_final_price',
        read_only=True
    )

    class Meta: 
        model = OrderItem
        fields = '__all__'



class OrderDetailsSerializer(serializers.ModelSerializer):
    customer = CustomerMinifiedSerializer()
    products = OrderItemSerializer(many=True, read_only=True)
    total_price = serializers.ReadOnlyField(
        source='get_total',
        read_only=True
    )
    class Meta:
        model = Order
        fields = ('id','customer','products', 'total_price')


class OrderSerializer(serializers.ModelSerializer):
    total_price = serializers.ReadOnlyField(
        source='get_total',
        read_only=True
    )
    class Meta:
        model = Order
        fields = '__all__'
