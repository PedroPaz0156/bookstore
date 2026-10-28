import pytest
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient


@pytest.fixture
def user(db):
    User = get_user_model()
    return User.objects.create_user(
        username="testuser",
        password="testpassword123",
    )


@pytest.fixture
def api_client(user):
    token, _ = Token.objects.get_or_create(user=user)

    client = APIClient()
    client.credentials(
        HTTP_AUTHORIZATION=f"Token {token.key}"
    )

    return client