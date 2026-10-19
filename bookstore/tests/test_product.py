import pytest

from product.models.product import Product 

@pytest.mark.django_db
def test_product_creation():
    product = Product.objects.create(
        name="Test Product",
        description="This is a test product.",
        price=20,
    )

    assert product.name == "Test Product"
    assert product.description == "This is a test product."
    assert product.price == 20
    assert product.id is not None