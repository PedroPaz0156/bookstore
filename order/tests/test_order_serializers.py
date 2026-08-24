import pytest

from order.serializers import OrderSerializer

@pytest.mark.django_db
def test_order_serializer():
    order_data = {
        "product": [
            {
                "title": "Test Product",
                "description": "This is a test product.",
                "price": 19.99
            }
        ],
        "user": {
            "username": "testuser",
            "password": "testpassword"
        }
    }

    serializer = OrderSerializer(data=order_data)

    assert serializer.is_valid()

    order = serializer.save()
    
    assert order.product.first().title == "Test Product"
    assert order.product.first().description == "This is a test product."
    assert order.product.first().price == 19.99
    assert order.user.username == "testuser"
    assert order.user.password == "testpassword"