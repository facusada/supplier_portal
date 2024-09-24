from rest_framework import serializers
from suppliers.models.order import Order
from suppliers.models.product import Product


class OrderSerializer(serializers.ModelSerializer):
    products = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(), many=True)

    class Meta:
        model = Order
        fields = ['id', 'order_date', 'status', 'total_amount', 'supplier', 'products']