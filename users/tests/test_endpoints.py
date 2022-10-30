import pytest
from rest_framework import status
from rest_framework.test import APIClient
from users.models import User


@pytest.mark.django_db
def test_retrieve_a_non_existing_user():
    client = APIClient()
    response = client.get('/users/1/')
    
    assert response.status_code == status.HTTP_404_NOT_FOUND
    
@pytest.mark.django_db
def test_retrieve_user_with_the_same_user(auth_client):
    user = User.objects.create_user(username = "mahmoud_aboelsoud", email = "mail@mail.com", password = "Password#1")
    
    client = auth_client(user)
    response = client.get('/users/1/')
    data = response.data
    
    assert response.status_code == status.HTTP_200_OK
    assert data['id'] == 1
    assert data['username'] == 'mahmoud_aboelsoud'
    assert data['email'] == "mail@mail.com"
    assert "password" not in data

@pytest.mark.django_db
def test_update_user_wtih_the_same_user(auth_client):
    user = User.objects.create_user(username = "mahmoud_aboelsoud", email = "mail@mail.com", password = "Password#1")

    client = auth_client(user)

    new_data = {
        'username' : 'mahmoudAboelsoud',
        'email' : 'mai@mail.com',
        'bio' : 'new bio'
    }

    response = client.put('/users/1/', new_data)
    data = response.data

    assert response.status_code == status.HTTP_200_OK
    assert data['id'] == 1
    assert data['username'] == new_data['username']
    assert data['email'] == new_data['email']
    assert data['bio'] == new_data['bio']
    assert 'password' not in data

@pytest.mark.django_db
def test_update_user_wtih_the_same_user_with_missing_fields(auth_client):
    user = User.objects.create_user(username = "mahmoud_aboelsoud", email = "mail@mail.com", password = "Password#1")

    client = auth_client(user)

    new_data = {
        'username' : 'mahmoudAboelsoud',
        'bio' : 'new bio'
    }

    response = client.put('/users/1/', new_data)
    data = response.data

    assert response.status_code == status.HTTP_200_OK
    assert data['id'] == 1
    assert data['username'] == new_data['username']
    assert data['email'] == "mail@mail.com"
    assert data['bio'] == new_data['bio']
    assert 'password' not in data

@pytest.mark.django_db
def test_partial_update_user_wtih_the_same_user(auth_client):
    user = User.objects.create_user(username = "mahmoud_aboelsoud", email = "mail@mail.com", password = "Password#1")

    client = auth_client(user)

    new_data = {
        'username' : 'mahmoudAboelsoud',
        'email' : 'mai@mail.com',
        'bio' : 'new bio'
    }

    response = client.patch('/users/1/', new_data)
    data = response.data

    assert response.status_code == status.HTTP_200_OK
    assert data['id'] == 1
    assert data['username'] == new_data['username']
    assert data['email'] == new_data['email']
    assert data['bio'] == new_data['bio']
    assert 'password' not in data

@pytest.mark.django_db
def test_partial_update_user_wtih_the_same_user_with_missing_fields(auth_client):
    user = User.objects.create_user(username = "mahmoud_aboelsoud", email = "mail@mail.com", password = "Password#1")

    client = auth_client(user)

    new_data = {
        'bio' : 'new bio'
    }

    response = client.patch('/users/1/', new_data)
    data = response.data

    assert response.status_code == status.HTTP_200_OK
    assert data['id'] == 1
    assert data['username'] == "mahmoud_aboelsoud"
    assert data['email'] == "mail@mail.com"
    assert data['bio'] == new_data['bio']
    assert 'password' not in data

@pytest.mark.django_db
def test_retrive_user_with_another_authenticated_user(auth_client):
    user = User.objects.create_user(username = "mahmoud_aboelsoud", email = "mail@mail.com", password = "Password#1")

    client = auth_client()

    response = client.get(f'/users/{user.id}/')
    data = response.data
    
    assert response.status_code == status.HTTP_200_OK
    assert data['id'] == 1
    assert data['username'] == 'mahmoud_aboelsoud'
    assert data['email'] == "mail@mail.com"
    assert "password" not in data

@pytest.mark.django_db
def test_update_user_with_another_authenticated_user(auth_client):
    user = User.objects.create_user(username = "mahmoud_aboelsoud", email = "mail@mail.com", password = "Password#1")

    client = auth_client()

    new_data = {
        'username' : 'mahmoudAboelsoud',
        'email' : 'lol@email.com',
        'bio' : 'hacked'
    }

    response = client.put(f'/users/{user.id}/', new_data)
    
    assert response.status_code == status.HTTP_403_FORBIDDEN

@pytest.mark.django_db
def test_partial_update_user_with_another_authenticated_user(auth_client):
    user = User.objects.create_user(username = "mahmoud_aboelsoud", email = "mail@mail.com", password = "Password#1")

    client = auth_client()

    new_data = {
        'email' : 'lol@email.com',
        'bio' : 'hacked'
    }

    response = client.patch(f'/users/{user.id}/', new_data)
    
    assert response.status_code == status.HTTP_403_FORBIDDEN

@pytest.mark.django_db
def test_retrive_user_with_non_authenticated_user():
    user = User.objects.create_user(username = "mahmoud_aboelsoud", email = "mail@mail.com", password = "Password#1")

    client = APIClient()
    response = client.get(f'/users/{user.id}/')
    data = response.data
    
    assert response.status_code == status.HTTP_200_OK
    assert data['id'] == 1
    assert data['username'] == 'mahmoud_aboelsoud'
    assert data['email'] == "mail@mail.com"
    assert "password" not in data

@pytest.mark.django_db
def test_update_user_with_non_authenticated_user():
    user = User.objects.create_user(username = "mahmoud_aboelsoud", email = "mail@mail.com", password = "Password#1")

    client = APIClient()

    new_data = {
        'username' : 'mahmoudAboelsoud',
        'email' : 'lol@email.com',
        'bio' : 'hacked'
    }

    response = client.put(f'/users/{user.id}/', new_data)
    
    assert response.status_code == status.HTTP_401_UNAUTHORIZED

@pytest.mark.django_db
def test_partial_update_user_with_non_authenticated_user():
    user = User.objects.create_user(username = "mahmoud_aboelsoud", email = "mail@mail.com", password = "Password#1")

    client = APIClient()

    new_data = {
        'email' : 'lol@email.com',
        'bio' : 'hacked'
    }

    response = client.patch(f'/users/{user.id}/', new_data)
    
    assert response.status_code == status.HTTP_401_UNAUTHORIZED
