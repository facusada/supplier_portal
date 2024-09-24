from rest_framework import serializers
from suppliers.models.product import Product
from suppliers.models.supplier import Supplier


class ProductSerializer(serializers.ModelSerializer):
    supplier = serializers.PrimaryKeyRelatedField(queryset=Supplier.objects.all())

    class Meta:
        model = Product
        fields = '__all__'