import pytest

from product.serializers.category_serializer import CategorySerializer

@pytest.mark.django_db
def test_category_serializer():
    category_data = {
        "title": "Test Category",
        "slug": "test-category",
        "description": "This is a test category.",
        "active": True
    }

    serializer = CategorySerializer(data=category_data)

    assert serializer.is_valid()

    category = serializer.save()

    serializer = CategorySerializer(category)
    serialized_data = serializer.data
    
    assert serialized_data["title"] == category_data["title"]
    assert serialized_data["description"] == category_data["description"]
    assert serialized_data["slug"] == category_data["slug"]
    assert serialized_data["active"] == category_data["active"]