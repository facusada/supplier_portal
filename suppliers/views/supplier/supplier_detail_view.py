from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from ...serializers.supplier_serializer import SupplierSerializer
from ...services.supplier_service import delete_supplier, get_supplier_by_id, update_supplier


class SupplierDetailView(APIView):
    def get(self, request, supplier_id):
        try:
            supplier = get_supplier_by_id(supplier_id)
            serializer = SupplierSerializer(supplier)
            return Response(serializer.data)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_404_NOT_FOUND)
            

    def put(self, request, supplier_id):
        try:
            supplier = update_supplier(supplier_id, request.data)
            serializer = SupplierSerializer(supplier)
            return Response(serializer.data)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, supplier_id):
        try:
            delete_supplier(supplier_id)
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
