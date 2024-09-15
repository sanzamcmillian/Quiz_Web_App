import pytest
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.test import APIClient


User = get_user_model()

@pytest.fixture()
@pytest.mark.django_db
def setup_users():
    client = APIClient()

    siba_registration_data = {
        'username': 'siba',
        'email': 'siba@localhost',
        'password': 'siba12345',
    }

    siba_login_data = {
        'username': 'siba',
        'password': 'siba12345',
    }

    registration_response = client.post("/auth/users/", siba_registration_data)

    login_response = client.post(reverse("users:login"), siba_login_data)

    return {
        'client': client,
        'registration_response': registration_response,
        'login_response': login_response
        }
