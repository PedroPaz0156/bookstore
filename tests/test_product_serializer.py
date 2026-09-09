import pytest

from product.models.product import Product
from product.serializers.product_serializer import ProductSerializer

@pytest.mark.django_db
def test_product_serializer():
    category_data = {
        "title": "Test Category",
        "description": "This is a test category.",
        "slug": "test-category"
    }

    product_data = {
        "name": "Test Product",
        "description": "This is a test product.",
        "price": 20,
        "category": category_data
    }

    serializer = ProductSerializer(data=product_data)

    assert serializer.is_valid(), f"Serializer errors: {serializer.errors}"

    product = serializer.save()

    serializer = ProductSerializer(product)
    serialized_data = serializer.data
    
    assert serialized_data["name"] == product_data["name"]
    assert serialized_data["description"] == product_data["description"]
    assert serialized_data["price"] == product_data["price"]
    assert serialized_data["category"]["title"] == category_data["title"]
    assert serialized_data["category"]["description"] == category_data["description"]
    assert serialized_data["category"]["slug"] == category_data["slug"]