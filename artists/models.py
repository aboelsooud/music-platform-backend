from django.db import models
from django.forms import CharField, URLField

# Create your models here.


class Artist(models.Model):
    stage_name = models.CharField(max_length=200, unique=True)
    social_link = models.URLField(max_length=200, blank=True, null=False)

    class Meta:
        ordering = ['stage_name']

    def __str__(self):
        return self.stage_name 
