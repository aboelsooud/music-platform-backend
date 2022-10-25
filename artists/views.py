from artists.models import Artist
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import ArtistSerializer

# Create your views here.

class ArtistApiView(APIView):
    def get(self, request):
        data = Artist.objects.all()
        seri = ArtistSerializer(data, many = True)
        return Response(seri.data)
    
    def post(self, request):
        seri = ArtistSerializer(data = request.data)
        if seri.is_valid():
            try:
                Artist.objects.get(stage_name = seri.validated_data.stage_name)
            except:
                seri.save()
                return Response(seri.data, status=status.HTTP_201_CREATED)
        
        return Response(seri.errors, status=status.HTTP_400_BAD_REQUEST)
