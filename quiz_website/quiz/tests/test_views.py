import pytest
from django.urls import reverse
from rest_framework import status

from users.models import *


@pytest.mark.django_db
def test_user_flow(client):
    siba_registration_data = {
        "username": "siba_the_first",
        "email": "siba@gmail.com",
        "password": "Nandipha12345",
    }

    siba_login_data = {
        "username": "siba_the_first",
        "password": "Nandipha12345",
    }

    registration_response = client.post("/auth/users/", siba_registration_data)
    print(registration_response.data)

    login_response = client.post("/account/login/", siba_login_data)

    print(login_response.data)
