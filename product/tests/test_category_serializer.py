import pytest

import product.serializers as CategorySerializer

@pytest.mark.django_db
def test_category_serializer():
    category_data = {
        "title": "Test Category",
        "description": "This is a test category."
    }

    serializer = CategorySerializer.CategorySerializer(data=category_data)

    assert serializer.is_valid()

    category = serializer.save()
    
    assert category.title == "Test Category"
    assert category.description == "This is a test category."