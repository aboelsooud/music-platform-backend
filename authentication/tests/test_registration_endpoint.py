import pytest
from rest_framework import status
from rest_framework.test import APIClient


@pytest.mark.django_db
def test_register_with_correct_data():
    user = {
        'username' : "mahmoud_aboelsoud",
        'email' : "mail@mail.com",
        'password' : "Password#1",
        'confirm_password' : "Password#1"
    }

    client = APIClient()
    response = client.post('/authentication/register/', user)
    data = response.data

    assert response.status_code == status.HTTP_200_OK
    assert data['user']['username'] == user['username']
    assert data['user']['email'] == user['email']
    assert 'password' not in data
    assert 'password' not in data['user']
    assert 'token' in data
    assert 'bio' in data['user']
    assert 'id' in data['user']

@pytest.mark.django_db
def test_register_with_some_missing_fields1():
    user = {
        'username' : "mahmoud_aboelsoud",
        'password' : "Password#1",
        'confirm_password' : "Password#1"
    }

    client = APIClient()
    response = client.post('/authentication/register/', user)

    assert response.status_code == status.HTTP_400_BAD_REQUEST

@pytest.mark.django_db
def test_register_with_some_missing_fields2():
    user = {
        'username' : "mahmoud_aboelsoud",
        'email' : "mail@mail.com",
        'password' : "Password#1",
    }

    client = APIClient()
    response = client.post('/authentication/register/', user)

    assert response.status_code == status.HTTP_400_BAD_REQUEST

@pytest.mark.django_db
def test_register_with_existing_mail():
    user1 = {
        'username' : "mahmoud_aboelsoud",
        'email' : "mail@mail.com",
        'password' : "Password#1",
        'confirm_password' : "Password#1"
    }

    client = APIClient()
    client.post('/authentication/register/', user1)

    user2 = {
        'username' : "mahmoudAboelsoud",
        'email' : "mail@mail.com",
        'password' : "Password#1",
        'confirm_password' : "Password#1"
    }

    client = APIClient()
    response = client.post('/authentication/register/', user2)

    assert response.status_code == status.HTTP_400_BAD_REQUEST

@pytest.mark.django_db
def test_register_with_existing_username():
    user1 = {
        'username' : "mahmoud_aboelsoud",
        'email' : "mail@mail.com",
        'password' : "Password#1",
        'confirm_password' : "Password#1"
    }

    client = APIClient()
    client.post('/authentication/register/', user1)

    user2 = {
        'username' : "mahmoud_aboelsoud",
        'email' : "mail@mailx.com",
        'password' : "Password#1",
        'confirm_password' : "Password#1"
    }

    client = APIClient()
    response = client.post('/authentication/register/', user2)

    assert response.status_code == status.HTTP_400_BAD_REQUEST

@pytest.mark.django_db
def test_register_with_weak_password():
    user = {
        'username' : "mahmoud_aboelsoud",
        'email' : "mail@mail.com",
        'password' : "123456python",
        'confirm_password' : "123456python"
    }

    client = APIClient()
    response = client.post('/authentication/register/', user)

    assert response.status_code == status.HTTP_400_BAD_REQUEST

@pytest.mark.django_db
def test_register_with_not_matching_passwords():
    user = {
        'username' : "mahmoud_aboelsoud",
        'email' : "mail@mail.com",
        'password' : "Password#1",
        'confirm_password' : "Password#2"
    }

    client = APIClient()
    response = client.post('/authentication/register/', user)

    assert response.status_code == status.HTTP_400_BAD_REQUEST
