from django.contrib import admin
from .models import Album
from django import forms
# Register your models here.

class AlbumForm(forms.ModelForm):

    class Meta:
        model = Album
        help_texts = {'is_explict' : 'Approve the album if its name is not explicit'}
        exclude = () 


class AlbumAdmin(admin.ModelAdmin):
    form = AlbumForm
    fieldsets = [
        ('Album data', {'fields' : ['name', 'artist',]}),
        ('Date information', {'fields': ['creation_date', 'release_date']}),
        (None,  {'fields': ['is_explict']}),
        (None,  {'fields': ['cost']}),
    ]

    readonly_fields = ['creation_date']


admin.site.register(Album, AlbumAdmin)
