from django.db import models
from artists.models import Artist

# Create your models here.

class Album(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    name = models.CharField(max_length = 200, default="New Album")
    creation_date = models.DateTimeField('Creation Date')
    release_date = models.DateTimeField(blank=False)
    cost = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name
