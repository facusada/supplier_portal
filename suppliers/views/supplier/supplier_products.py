from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from suppliers.services.supplier_service import get_supplier_products
from suppliers.serializers.product_serializer import ProductSerializer

class SupplierProductsView(APIView):
    def get(self, request, supplier_id):
        try:
            products = get_supplier_products(supplier_id)
            serializer = ProductSerializer(products, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        except ValueError as ve:
            return Response({"error": str(ve)}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)