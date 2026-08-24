import pytest

from product.serializers import ProductSerializer

@pytest.mark.django_db
def test_product_serializer():
    product_data = {
        "title": "Test Product",
        "description": "This is a test product.",
        "price": 19.99
    }

    serializer = ProductSerializer(data=product_data)

    assert serializer.is_valid()

    product = serializer.save()
    
    assert product.title == "Test Product"
    assert product.description == "This is a test product."
    assert product.price == 19.99