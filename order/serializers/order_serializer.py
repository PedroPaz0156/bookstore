from django.contrib.auth import get_user_model
from rest_framework import serializers
from order.models.order import Order
from product.models.product import Product
from product.serializers.product_serializer import ProductSerializer

User = get_user_model()


class OrderSerializer(serializers.ModelSerializer):
    product = ProductSerializer(many=True, required=True)
    user = serializers.DictField(write_only=True, required=True)
    user_id = serializers.IntegerField(read_only=True)
    total = serializers.SerializerMethodField()

    def get_total(self, instance):
        return sum((product.price or 0) for product in instance.product.all())

    class Meta:
        model = Order
        fields = ["id", "product", "user", "user_id", "total"]
        read_only_fields = ["id", "user_id", "total"]

    def create(self, validated_data):
        products_data = validated_data.pop("product")
        user_data = validated_data.pop("user")
        username, password = user_data.get("username"), user_data.get("password")
        if not username or not password:
            raise serializers.ValidationError({"user": "username and password are required."})
        user, created = User.objects.get_or_create(
            username=username,
            defaults={key: value for key, value in user_data.items() if key != "password"},
        )
        if created:
            user.set_password(password)
            user.save(update_fields=["password"])
        products = []
        for product_data in products_data:
            category_data = product_data.pop("category", None)
            category = None
            if category_data:
                from product.models.category import Category
                slug = category_data.get("slug")
                category = Category.objects.filter(slug=slug).first() if slug else None
                if category is None:
                    category = Category.objects.create(**category_data)
            products.append(Product.objects.create(category=category, **product_data))
        order = Order.objects.create(user=user, **validated_data)
        order.product.set(products)
        return order

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["product"] = ProductSerializer(instance.product.all(), many=True).data
        data["user"] = {"username": instance.user.username}
        return data
