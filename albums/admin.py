from django.contrib import admin
from .models import Album, Song
from django import forms

# Register your models here.

class SongsInline(admin.StackedInline):
    model = Song
    extra = 0

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        help_texts = {'is_approved_by_admin' : 'Approve the album if its name is not explicit'}
        exclude = () 

class AlbumAdmin(admin.ModelAdmin):
    form = AlbumForm

    fieldsets = [
        ('Album data', {'fields' : ['name', 'artist',]}),
        ('Date information', {'fields': ['release_date']}),
        (None,  {'fields': ['is_approved_by_admin']}),
        (None,  {'fields': ['cost']}),
    ]

    inlines = [SongsInline]

admin.site.register(Album, AlbumAdmin)
