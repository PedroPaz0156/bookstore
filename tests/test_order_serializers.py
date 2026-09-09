import pytest

from order.serializers.order_serializer import OrderSerializer

@pytest.mark.django_db
def test_order_serializer():
    order_data = {
        "product": [
            {
                "name": "Test Product",
                "description": "This is a test product.",
                "price": 20,
                "category": {
                    "title": "Test Category",
                    "description": "This is a test category.",
                    "slug": "test-category"
                }
            }
        ],
        "user": {
            "username": "testuser",
            "password": "testpassword"
        }
    }

    serializer = OrderSerializer(data=order_data)

    assert serializer.is_valid(), f"Serializer errors: {serializer.errors}"

    order = serializer.save()

    serializer = OrderSerializer(order)
    serialized_data = serializer.data
    
    assert serialized_data["product"][0]["name"] == order_data["product"][0]["name"]
    assert serialized_data["product"][0]["description"] == order_data["product"][0]["description"]
    assert serialized_data["product"][0]["price"] == order_data["product"][0]["price"]
    assert serialized_data["user"]["username"] == order_data["user"]["username"]
    assert serialized_data["user"]["password"] == order_data["user"]["password"]