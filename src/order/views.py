from rest_framework import generics, viewsets
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.views import APIView

from .models import Order, OrderItem
from .permissions import IsCustomerOrReadonly
from .serializers import OrderItemSerializer, OrderSerializer, OrderDetailsSerializer


class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all().order_by('id')
    serializer_class = OrderItemSerializer
    permission_classes = [IsAuthenticated , IsCustomerOrReadonly]



class OrderCreateApiView(generics.CreateAPIView):
    queryset = Order.objects.all().order_by('id')
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated ]


class OrderListApiView(generics.ListAPIView):
    serializer_class = OrderDetailsSerializer
    permission_classes = [IsAuthenticated , IsAdminUser]

    def get_queryset(self):
        qs =  Order.objects.all().order_by('id')
        location = self.request.query_params.get('location', None)
        if location is not None:
            qs  = Order.objects.filter(customer__location=location)
        return qs


class OrderRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated , IsCustomerOrReadonly]