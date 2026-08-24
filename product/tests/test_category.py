import pytest

from product.models import Category

@pytest.mark.django_db
def test_category_creation():
    category = Category.objects.create(
        title="Test Category",
        description="This is a test category."
    )

    assert category.title == "Test Category"
    assert category.description == "This is a test category."
    assert category.id is not None