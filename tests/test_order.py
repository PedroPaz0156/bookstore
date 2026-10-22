import pytest

from django.contrib.auth.models import User

from order.models.order import Order
from product.models.product import Product

@pytest.mark.django_db
def test_order_creation():
    user = User.objects.create_user(
        username="testuser",
        password="testpassword",
    )

    product = Product.objects.create(
        name="Test Product",
        description="This is a test product.",
        price=20,
    )

    order = Order.objects.create(user=user)
    order.product.set([product])

    assert order.product.count() == 1

    saved_product = order.product.first()
    assert saved_product.name == "Test Product"
    assert saved_product.description == "This is a test product."
    assert saved_product.price == 20

    assert order.user.username == "testuser"
    assert order.user.check_password("testpassword")
    assert order.id is not None