from django.db import models
from artists.models import Artist
from model_utils.models import TimeStampedModel

# Create your models here.

class Album(TimeStampedModel):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    name = models.CharField(max_length = 200, default="New Album")
    release_date = models.DateTimeField(blank=False)
    cost = models.DecimalField(max_digits=6, decimal_places=2)
    is_approved_by_admin = models.BooleanField(default=False, help_text = "Approve the album if its name is not explicit")

    def __str__(self):
        return self.name
