import pytest 

from product.models import Product

@pytest.mark.django_db
def test_product_creation():
    product = Product.objects.create(
        title="Test Product",
        description="This is a test product.",
        price=19.99
    )

    assert product.title == "Test Product"
    assert product.description == "This is a test product."
    assert product.price == 19.99
    assert product.id is not None