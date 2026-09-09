import pytest

from django.contrib.auth.models import User

from order.models.order import Order
from product.models.product import Product

@pytest.mark.django_db
def test_order_creation():
    order = Order.objects.create(
        product=Product.objects.create(name="Test Product",
                                        description="This is a test product.", 
                                        price=20),
        user=User.objects.create(username="testuser", password="testpassword"),
    )

    assert order.product.name == "Test Product"
    assert order.product.description == "This is a test product."
    assert order.product.price == 20
    assert order.user.username == "testuser"
    assert order.user.password == "testpassword"
    assert order.id is not None