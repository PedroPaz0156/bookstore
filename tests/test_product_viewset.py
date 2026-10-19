import pytest
from django.urls import reverse
from rest_framework.test import APIClient

from product.models.product import Product


@pytest.mark.django_db
def test_product_viewset_create_and_list():
    client = APIClient()
    payload = {
        "name": "Dom Casmurro",
        "description": "Romance de Machado de Assis",
        "price": 35,
        "active": True,
        "category": {
            "title": "Literatura brasileira",
            "slug": "literatura-brasileira",
            "description": "Clássicos brasileiros",
            "active": True,
        },
    }

    create_response = client.post(reverse("product-list"), payload, format="json")

    assert create_response.status_code == 201, create_response.data
    assert create_response.data["name"] == payload["name"]
    assert Product.objects.filter(name=payload["name"]).exists()

    list_response = client.get(reverse("product-list"))
    assert list_response.status_code == 200
    assert any(item["name"] == payload["name"] for item in list_response.data)
