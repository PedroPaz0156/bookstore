from rest_framework import serializers
from product.models.product import Product
from product.models.category import Category
from product.serializers.category_serializer import CategorySerializer


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(required=False, allow_null=True)

    class Meta:
        model = Product
        fields = ["id", "name", "description", "price", "active", "category"]
        read_only_fields = ["id"]

    def create(self, validated_data):
        category_data = validated_data.pop("category", None)
        category = None
        if category_data:
            category, _ = Category.objects.get_or_create(
                slug=category_data.get("slug") or "",
                defaults=category_data,
            )
            # If a slug was omitted, create through the model's slug generation.
            if not category.pk:
                category.save()
        return Product.objects.create(category=category, **validated_data)

    def update(self, instance, validated_data):
        category_data = validated_data.pop("category", serializers.empty)
        if category_data is not serializers.empty:
            if category_data is None:
                instance.category = None
            else:
                slug = category_data.get("slug")
                category = None
                if slug:
                    category = Category.objects.filter(slug=slug).first()
                if category is None:
                    category = Category.objects.create(**category_data)
                instance.category = category
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance
