from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError
from suppliers.serializers.order_serializer import OrderSerializer
from suppliers.services.order_service import create_order

class OrderCreateView(APIView):
    def post(self, request):
        try:
            serializer = OrderSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)

            order = create_order(serializer.validated_data)

            return Response(OrderSerializer(order).data, status=status.HTTP_201_CREATED)

        except ValidationError as ve:
            return Response({"error": str(ve)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)