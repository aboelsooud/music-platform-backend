import pytest
from artists.models import Artist
from rest_framework import status
from rest_framework.test import APIClient


@pytest.mark.django_db
def test_create_an_artist():
    client = APIClient()

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
def test_create_artist_with_existing_stage_name():
    client = APIClient()

    artist = {
        'stage_name' : 'Kendrick Lamar'
    }

    client.post('/artists/', artist)
    
    artist = {
        'stage_name' : 'Kendrick Lamar',
        'social_link' : 'https://www.instagram.com/kendricklamar/'
    }

    response = client.post('/artists/', artist)

    assert response.status_code == status.HTTP_400_BAD_REQUEST

@pytest.mark.django_db
def test_retriving_list_of_artists():
    client = APIClient()

    artist = {
        'stage_name' : 'Kendrick Lamar'
    }

    client.post('/artists/', artist)

    artist = {
        'stage_name' : 'Baby Keem'
    }

    client.post('/artists/', artist)

    artist = {
        'stage_name' : 'Frank Ocean'
    }

    client.post('/artists/', artist)

    response = client.get('/artists/')
    data = response.data

    assert response.status_code == status.HTTP_200_OK

    artists = Artist.objects.all().values()

    for i in range(len(data)):
        assert data[i] == artists[i]
