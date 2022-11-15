from django.contrib import admin

from .models import Artist

# Register your models here.

class ArtistAdmin(admin.ModelAdmin):
    list_display = ('stage_name', 'number_of_approved_albums', )
    
    def number_of_approved_albums(self, artist):
        return artist.album_set.filter(is_approved_by_admin = True).count()
    

admin.site.register(Artist, ArtistAdmin)
