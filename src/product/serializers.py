from rest_framework import serializers
from .models import Category, Product


class CategorySerializer(serializers.ModelSerializer):
    product_count = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Category
        fields = '__all__'

    def get_product_count(self, instance):
        return instance.products.count()

class ProductSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(read_only=True)

    class Meta:
        model = Product
        fields = '__all__'