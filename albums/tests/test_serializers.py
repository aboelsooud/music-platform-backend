from datetime import datetime
from decimal import Decimal

import pytest
from albums.models import Album
from albums.serializers import AlbumSerializer
from artists.models import Artist
from dateutil.parser import parse
from users.models import User


@pytest.mark.django_db
def test_serializer_returns_expected_fields_and_data():
    user = User.objects.create_user(username='user')
    artist = Artist.objects.create(user = user, stage_name = 'artist')
    album = Album.objects.create(artist = artist, name = 'album', release_date = datetime(2022, 10,10), cost = 100.10)

    seri = AlbumSerializer(album)

    assert seri.data['id'] == album.id
    assert seri.data['artist']['id'] == artist.id
    assert seri.data['artist']['stage_name'] == artist.stage_name
    assert seri.data['artist']['social_link'] == artist.social_link
    assert seri.data['name'] == album.name
    assert parse(seri.data['release_date'][:-1]) == album.release_date
    assert float(Decimal(seri.data['cost'])) == float(Decimal(album.cost))

@pytest.mark.django_db
def test_serializer_with_valid_data():
    seri = AlbumSerializer(data={
        "name": "album",
        "release_date": "2020-10-10",
        "cost": 100
    })

    seri.is_valid(raise_exception=False)
    assert not seri.errors
    assert seri.validated_data['name'] == 'album'
    assert float(seri.validated_data['cost']) == float(Decimal(100.00))    

@pytest.mark.django_db
def test_serializer_with_missing_data():
    seri = AlbumSerializer(data={
        "name": "album",
        "release_date": "2020-10-10",
    })

    seri.is_valid(raise_exception=False)
    assert seri.errors
    assert seri.errors.keys() == set(['cost'])

@pytest.mark.django_db
def test_serializer_with_wrong_data1():
    seri = AlbumSerializer(data={
        "name": "album",
        "release_date": "2020-10-10",
        "cost": "string"
    })

    seri.is_valid(raise_exception=False)
    assert seri.errors
    assert seri.errors.keys() == set(['cost'])

@pytest.mark.django_db
def test_serializer_with_worng_data2():
    seri = AlbumSerializer(data={
        "name": "album",
        "release_date": "10-5",
        "cost": 100
    })

    seri.is_valid(raise_exception=False)
    assert seri.errors
    assert seri.errors.keys() == set(['release_date'])
