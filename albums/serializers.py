from artists.models import Artist
from rest_framework import serializers

from .models import Album


class AlbumSerializer(serializers.ModelSerializer):
    artist = serializers.SerializerMethodField('_artist_data')

    def _artist_data(self, obj):
        artist = Artist.objects.get(pk = obj.artist.pk)
        return {
            'id' : artist.id,
            'stage_name' : artist.stage_name,
            'social_link' : artist.social_link
        }

    class Meta:
        model = Album
        fields = ('id', 'artist' ,'name','release_date', 'cost')
