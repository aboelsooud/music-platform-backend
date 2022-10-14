from django.contrib import admin
from .models import Artist

# Register your models here.

class ArtistAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Artist data', {'fields': ['stage_name', 'social_link']}),
    ]


admin.site.register(Artist, ArtistAdmin)
