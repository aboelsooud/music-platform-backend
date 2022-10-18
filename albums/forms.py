from django import forms

from .models import Album

class AlbumForm(forms.ModelForm):

    class Meta:
        model = Album
        fields = ('artist', 'name', 'release_date', 'cost')
