from decimal import Decimal
import pytest
from artists.models import Artist
from albums.models import Album
from rest_framework import status
from rest_framework.test import APIClient
from users.models import User
from datetime import datetime
import pytz


@pytest.mark.django_db
def test_create_an_album(auth_client):
    user = User.objects.create_user(username = 'user')
    artist = Artist.objects.create(user = user, stage_name = 'artist')

    client = auth_client(user)

    album = {
        "name" : "album1",
        "release_date": datetime(2020, 10, 10, tzinfo=pytz.UTC),
        "cost" : 100
    }

    response = client.post('/albums/', album)
    data = response.data

    assert response.status_code == status.HTTP_201_CREATED
    assert data['id'] == 1
    assert data['artist']['id'] == artist.id
    assert data['artist']['stage_name'] == artist.stage_name
    assert data['artist']['social_link'] == artist.social_link
    assert data['name'] == album['name']
    assert data['release_date'] == album['release_date'].strftime("%Y-%m-%dT%H:%M:%SZ")
    assert float(Decimal(data['cost'])) == float(Decimal(album['cost'])) 

@pytest.mark.django_db
def test_create_album_with_missing_fileds(auth_client):
    user = User.objects.create_user(username = 'user')
    artist = Artist.objects.create(user = user, stage_name = 'artist')

    client = auth_client(user)

    album = {
        "name" : "album1",
        "cost" : 100
    }

    response = client.post('/albums/', album)

    assert response.status_code == status.HTTP_400_BAD_REQUEST

@pytest.mark.django_db
def test_create_album_with_string_in_cost(auth_client):
    user = User.objects.create_user(username = 'user')
    artist = Artist.objects.create(user = user, stage_name = 'artist')

    client = auth_client(user)

    album = {
        "name" : "album1",
        "release_date": datetime(2020, 10, 10, tzinfo=pytz.UTC),
        "cost" : "string"
    }

    response = client.post('/albums/', album)

    assert response.status_code == status.HTTP_400_BAD_REQUEST

@pytest.mark.django_db
def test_create_an_album_with_unauthenticated_user():
    client = APIClient()

    album = {
        "name" : "album1",
        "release_date": datetime(2020, 10, 10, tzinfo=pytz.UTC),
        "cost" : 100
    }

    response = client.post('/albums/', album)

    assert response.status_code == status.HTTP_401_UNAUTHORIZED

@pytest.mark.django_db
def test_create_an_album_with_authenticated_user_who_is_not_an_artist(auth_client):
    client = auth_client()

    album = {
        "name" : "album1",
        "release_date": datetime(2020, 10, 10, tzinfo=pytz.UTC),
        "cost" : 100
    }

    response = client.post('/albums/', album)

    assert response.status_code == status.HTTP_403_FORBIDDEN

@pytest.mark.django_db
def test_retrieve_albums_data():
    user1 = User.objects.create_user(username='user1')
    user2 = User.objects.create_user(username='user2')
    user3 = User.objects.create_user(username='user3')
    
    artist1 = Artist.objects.create(user=user1, stage_name = 'artist1')
    artist2 = Artist.objects.create(user=user2, stage_name = 'artist2')
    artist3 = Artist.objects.create(user=user3, stage_name = 'artist3')
    
    album1 = Album.objects.create(artist = artist1, name = 'album1', release_date = datetime(2022, 10, 10, tzinfo=pytz.UTC), cost = 100, is_approved_by_admin = True)
    album2 = Album.objects.create(artist = artist1, name = 'album2', release_date = datetime(2021, 10, 10, tzinfo=pytz.UTC), cost = 99.99)
    album3 = Album.objects.create(artist = artist2, name = 'album3', release_date = datetime(2020, 10, 10, tzinfo=pytz.UTC), cost = 199.76, is_approved_by_admin = True)
    album4 = Album.objects.create(artist = artist3, name = 'album4', release_date = datetime(2022, 10, 10, tzinfo=pytz.UTC), cost = 88.52)
    
    albums = [album1, album3]

    client = APIClient()

    response = client.get('/albums/')
    data = response.data

    assert response.status_code == status.HTTP_200_OK
    assert len(data) != 4
    assert len(data) == 2

    for i in range(len(data)):
        assert albums[i].id == data[i]['id']
        assert albums[i].name == data[i]['name']
        assert albums[i].release_date.strftime("%Y-%m-%dT%H:%M:%SZ") == data[i]['release_date']
        assert float(Decimal(albums[i].cost)) == float(Decimal(data[i]['cost']))
        assert albums[i].artist.id == data[i]['artist']['id']
        assert albums[i].artist.stage_name == data[i]['artist']['stage_name']
        assert albums[i].artist.social_link == data[i]['artist']['social_link']
