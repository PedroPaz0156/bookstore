
import pytest
from rest_framework.test import APIClient
from django.urls import reverse

from product.models.category import Category


@pytest.mark.django_db
def test_category_viewset_create_and_list():
    client = APIClient()

    payload = {
        "title": "Ficção",
        "slug": "ficcao",
        "description": "Livros de histórias fictícias e imaginárias.",
        "active": True,
    }

    create_response = client.post(
        reverse("category-list"),
        payload,
        format="json",
    )

    assert create_response.status_code == 201, create_response.data
    assert create_response.data["title"] == payload["title"]
    assert Category.objects.filter(slug=payload["slug"]).exists()

    list_response = client.get(reverse("category-list"))

    assert list_response.status_code == 200

    data = list_response.data
    categories = data["results"] if isinstance(data, dict) and "results" in data else data

    assert any(
        item["slug"] == payload["slug"]
        for item in categories
    )
