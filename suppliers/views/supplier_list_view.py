from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from ..serializers.supplier_serializer import SupplierSerializer
from ..services.supplier_service import get_all_suppliers, create_supplier

class SupplierListView(APIView):
    def get(self, request):
        try:
            suppliers = get_all_suppliers()
            serializer = SupplierSerializer(suppliers, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request):
        try:
            serializer = SupplierSerializer(data=request.data)

            if serializer.is_valid():
                supplier = create_supplier(serializer.validated_data)
                return Response(SupplierSerializer(supplier).data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
