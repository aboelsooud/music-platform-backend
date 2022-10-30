import pytest

from rest_framework.test import APIClient
from rest_framework import status

@pytest.mark.django_db
def test_login_success():
    user = {
        'username' : "mahmoud_aboelsoud",
        'email' : "mail@mail.com",
        'password' : "Password#1",
        'confirm_password' : "Password#1"
    }

    client = APIClient()
    client.post('/authentication/register/', user)

    response = client.post('/authentication/login/', {'username' : "mahmoud_aboelsoud", 'password' : "Password#1",})
    
    assert response.status_code == status.HTTP_200_OK
    
    data = response.data

    assert data['user']['username'] == user['username']
    assert "email" in data['user']
    assert 'password' not in data
    assert 'password' not in data['user']
    assert 'token' in data
    assert 'bio' in data['user']
    assert 'id' in data['user']


@pytest.mark.django_db
def test_login_fail_not_a_user():
    client = APIClient()
    response = client.post('/authentication/login/', {'username' : "mahmoud_aboelsoud", 'password' : "Password#1",})

    assert response.status_code == status.HTTP_400_BAD_REQUEST

@pytest.mark.django_db
def test_login_fail_missing_fields():
    user = {
        'username' : "mahmoud_aboelsoud",
        'email' : "mail@mail.com",
        'password' : "Password#1",
        'confirm_password' : "Password#1"
    }

    client = APIClient()
    client.post('/authentication/register/', user)

    response = client.post('/authentication/login/', {'username' : "mahmoud_aboelsoud",})
    
    assert response.status_code == status.HTTP_400_BAD_REQUEST
