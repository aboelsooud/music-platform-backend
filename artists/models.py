from django.db import models
from django.db.models import Count, Q

# Create your models here.

class ArtistQuerySet(models.QuerySet):
    def annotated(self):
        return self.annotate(approved_albums=Count('album', filter=Q(album__is_approved_by_admin=True)))

class ArtistManager(models.Manager):
    def get_queryset(self):
        return ArtistQuerySet(self.model, using=self._db)
    
    def annotated(self):
        return self.get_queryset().annotated()


class Artist(models.Model):
    stage_name = models.CharField(max_length=200, unique=True)
    social_link = models.URLField(max_length=200, blank=True, null=False)
    objects = ArtistManager()

    class Meta:
        ordering = ['stage_name']

    def __str__(self):
        return self.stage_name
