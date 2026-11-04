import pytest
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.test import APIClient

from order.models.order import Order


@pytest.mark.django_db
def test_order_viewset_create_and_list(api_client):
    payload = {
        "product": [
            {
                "name": "O Hobbit",
                "description": "Fantasia",
                "price": 42,
                "active": True,
                "category": {
                    "title": "Fantasia",
                    "slug": "fantasia",
                    "description": "Livros de fantasia",
                    "active": True,
                },
            }
        ],
        "user": {
            "username": "cliente_viewset",
            "password": "senha-de-teste-segura",
        },
    }

    create_response = api_client.post(reverse("order-list"), payload, format="json")

    assert create_response.status_code == 201, create_response.data
    assert create_response.data["user"]["username"] == payload["user"]["username"]
    assert "password" not in create_response.data["user"]
    assert Order.objects.filter(user__username=payload["user"]["username"]).exists()
    assert User.objects.filter(username=payload["user"]["username"]).exists()

    list_response = api_client.get(reverse("order-list"))
    assert list_response.status_code == 200
    assert any(
        item["user"]["username"] == payload["user"]["username"]
        for item in list_response.data["results"]
    )
