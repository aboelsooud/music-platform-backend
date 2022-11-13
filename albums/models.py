from django.db import models
from artists.models import Artist
from model_utils.models import TimeStampedModel
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from django.core.validators import FileExtensionValidator
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify

# Create your models here.

class Album(TimeStampedModel):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    name = models.CharField(max_length = 200, default="New Album")
    release_date = models.DateTimeField(blank=False)
    cost = models.DecimalField(max_digits=6, decimal_places=2)
    is_approved_by_admin = models.BooleanField(default=False, help_text = "Approve the album if its name is not explicit")

    def __str__(self):
        return self.name

class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    name = models.SlugField(max_length = 200, blank=True)
    image = models.ImageField(upload_to='images/', blank=True)
    image_thumbnail = ProcessedImageField(upload_to='covers/', processors=[ResizeToFill(100, 50)], format='JPEG', options={'quality': 60}, blank = True)
    audio = models.FileField(upload_to='songs/', validators = [FileExtensionValidator(allowed_extensions=["mp3", "wav"])], blank = True)

    def __str__(self):
        return self.name

@receiver(pre_save, sender=Song)
def song_pre_save(sender, instance, *args, **kwargs):
    if len(instance.name.strip()) == 0:
        instance.name = slugify(instance.album.name)
