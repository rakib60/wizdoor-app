from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (OrderCreateApiView, OrderItemViewSet, OrderListApiView,
                    OrderRUDAPIView)

router = DefaultRouter()
router.register(r"orderItem", OrderItemViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path('order/', OrderCreateApiView.as_view(), name='create-order'),
    path('orders/', OrderListApiView.as_view(), name='order-list'),
    path('orders/<int:pk>/', OrderRUDAPIView.as_view(), name='order-details'),
]
