from artists.models import Artist
from .serializers import ArtistSerializer
from rest_framework import generics

# Create your views here.

class ArtistApiView(generics.ListCreateAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
