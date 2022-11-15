import pytest
from artists.models import Artist
from rest_framework import status
from rest_framework.test import APIClient
from users.models import User


@pytest.mark.django_db
def test_create_an_artist(auth_client):
    client = auth_client()

    artist = {
        'stage_name' : 'Kendrick Lamar'
    }

    response = client.post('/artists/', artist)
    data = response.data

    assert response.status_code == status.HTTP_201_CREATED
    assert data['id'] == 1
    assert data['stage_name'] == artist['stage_name']
    assert 'social_link' in data

@pytest.mark.django_db
def test_create_artist_with_existing_stage_name(auth_client):
    user1 = User.objects.create_user(username = 'user1')
    user2 = User.objects.create_user(username = 'user2')
    
    client1 = auth_client(user1)
    client2 = auth_client(user2)

    artist = {
        'stage_name' : 'Kendrick Lamar'
    }

    client1.post('/artists/', artist)
    
    artist = {
        'stage_name' : 'Kendrick Lamar',
        'social_link' : 'https://www.instagram.com/kendricklamar/'
    }

    response = client2.post('/artists/', artist)

    assert response.status_code == status.HTTP_400_BAD_REQUEST

@pytest.mark.django_db
def test_create_artist_with_unauthenticated_user():
    client = APIClient()
    artist = {
        'stage_name' : 'Kendrick Lamar'
    }

    response = client.post('/artists/', artist)

    assert response.status_code == status.HTTP_401_UNAUTHORIZED

@pytest.mark.django_db
def test_creating_2_artists_with_the_same_user(auth_client):
    client = auth_client()

    artist = {
        'stage_name' : 'Kendrick Lamar'
    }

    client.post('/artists/', artist)

    artist = {
        'stage_name' : 'Baby Keem'
    }

    response = client.post('/artists/', artist)

    assert response.status_code == status.HTTP_400_BAD_REQUEST

@pytest.mark.django_db
def test_retriving_list_of_artists(auth_client):
    user1 = User.objects.create_user(username = "user1")
    user2 = User.objects.create_user(username = "user2")
    user3 = User.objects.create_user(username = "user3")

    client1 = auth_client(user1)
    client2 = auth_client(user2)
    client3 = auth_client(user3)

    artist = {
        'stage_name' : 'Kendrick Lamar'
    }

    client1.post('/artists/', artist)

    artist = {
        'stage_name' : 'Baby Keem'
    }

    client2.post('/artists/', artist)

    artist = {
        'stage_name' : 'Frank Ocean'
    }

    client3.post('/artists/', artist)

    response = client1.get('/artists/')
    data = response.data

    assert response.status_code == status.HTTP_200_OK

    artists = Artist.objects.all().values()

    for i in range(len(data)):
        assert artists[i]['id'] == data[i]['id']
        assert artists[i]['stage_name'] == data[i]['stage_name']
        assert artists[i]['social_link'] == data[i]['social_link']
        assert 'user_id' in artists[i]
