from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from ...serializers.supplier_serializer import SupplierSerializer
from ...services.supplier_service import search_suppliers

class SupplierSearchView(APIView):
    def get(self, request):
        try:
            name = request.query_params.get('name')
            email = request.query_params.get('email')
            tax_id = request.query_params.get('tax_id')
            
            suppliers = search_suppliers(name=name, email=email, tax_id=tax_id)
            serializer = SupplierSerializer(suppliers, many=True)

            return Response(serializer.data, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({"message": "No suppliers found"}, status=status.HTTP_404_NOT_FOUND)
