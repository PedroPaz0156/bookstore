from rest_framework import serializers

from product.models.product import Product
from product.serializers.category_serializer import CategorySerializer

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=False, required=True)

    class Meta:
        model = Product
        fields = [
            'name',
            'description',
            'price',
            'active',
            'category',
        ]

    def create(self, validated_data):
        category_data = validated_data.pop('category')
        category_serializer = CategorySerializer(data=category_data)
        category_serializer.is_valid(raise_exception=True)
        category = category_serializer.save()
        product = Product.objects.create(category=category, **validated_data)
        return product