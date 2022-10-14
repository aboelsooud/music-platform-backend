from django.contrib import admin
from .models import Album

# Register your models here.

class AlbumAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Album data', {'fields' : ['name', 'artist',]}),
        ('Date information', {'fields': ['creation_date', 'release_date']}),
        (None,  {'fields': ['is_explict']}),
        (None,  {'fields': ['cost']}),
    ]

    readonly_fields = ['creation_date']


admin.site.register(Album, AlbumAdmin)
