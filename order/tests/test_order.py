import pytest

from django.contrib.auth.models import User

from order.models import Order
from product.models import Product

@pytest.mark.django_db
def test_order_creation():
    order = Order.objects.create(
        product=Product.objects.create(title="Test Product",
                                        description="This is a test product.", 
                                        price=19.99),
        user=User.objects.create(username="testuser", password="testpassword"),
    )

    assert order.product.title == "Test Product"
    assert order.product.description == "This is a test product."
    assert order.product.price == 19.99
    assert order.user.username == "testuser"
    assert order.user.password == "testpassword"
    assert order.id is not None