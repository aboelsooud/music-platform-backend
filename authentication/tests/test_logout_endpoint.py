import pytest
from rest_framework import status
from rest_framework.test import APIClient


@pytest.mark.django_db
def test_logout_success(auth_client):
    client = auth_client()
    response = client.post('/authentication/logout/')

    assert response.status_code == status.HTTP_204_NO_CONTENT

@pytest.mark.django_db
def test_logout_fail():
    client = APIClient()
    response = client.post('/authentication/logout/')

    assert response.status_code == status.HTTP_401_UNAUTHORIZED
