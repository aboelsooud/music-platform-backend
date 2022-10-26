from artists.models import Artist
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import ArtistSerializer
from rest_framework import generics

# Create your views here.

class ArtistApiView(generics.ListCreateAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
