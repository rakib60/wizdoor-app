from rest_framework import generics, viewsets
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.generics import get_object_or_404

from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by('-id')
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated, IsAdminUser]


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('-id')
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

    # def perform_create(self, serializer):
    #     kwarg_slug = self.kwargs.get("slug")
    #     product = get_object_or_404(Product, slug=kwarg_slug)

    #     if product.exists():
    #         raise ValidationError("You have already this Product!")

    #     serializer.save(product=product)
