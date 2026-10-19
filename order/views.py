from rest_framework import viewsets
from order.models.order import Order
from order.serializers.order_serializer import OrderSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.prefetch_related("product").select_related("user").all()
    serializer_class = OrderSerializer
