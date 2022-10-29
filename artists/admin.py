from django.contrib import admin
from .models import Artist
from albums.models import Album

# Register your models here.

class AlbumsInlineAdmin(admin.TabularInline):
    model = Album
    extra = 0

class ArtistAdmin(admin.ModelAdmin):
    list_display = ('stage_name', 'number_of_approved_albums', )
    
    def number_of_approved_albums(self, artist):
        return artist.album_set.filter(is_approved_by_admin = True).count()
    
    fieldsets = [
        ('Artist data', {'fields': ['stage_name', 'social_link']}),
    ]

    inlines = [AlbumsInlineAdmin]

admin.site.register(Artist, ArtistAdmin)
