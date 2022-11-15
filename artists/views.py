from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from artists.models import Artist

from .serializers import ArtistSerializer


class ArtistApiView(GenericAPIView):
    serializer_class = ArtistSerializer
    queryset = Artist.objects.all()

    def get(self, request):
        data = Artist.objects.all()
        seri = ArtistSerializer(data, many = True)
        return Response(seri.data)

    def post(self, request):
        if hasattr(request.user, 'artist'):
            return Response(data={'status': status.HTTP_400_BAD_REQUEST,'message':'this user is already an artist'}, status=status.HTTP_400_BAD_REQUEST, )
        
        if not request.user.is_authenticated:
            return Response(status=status.HTTP_401_UNAUTHORIZED, data = {'status': status.HTTP_401_UNAUTHORIZED,'message':'this user is not authenticated'})
        
        seri = ArtistSerializer(data = request.data)
        seri.is_valid(raise_exception=True)

        try: 
            Artist.objects.get(stage_name = seri.validated_data['stage_name'])
        except:
            artist = None
            if 'social_link' in seri.validated_data:
               artist = Artist.objects.create(user = request.user, stage_name = seri.validated_data['stage_name'], social_link = seri.validated_data['social_link'])
            else:
                artist = Artist.objects.create(user = request.user, stage_name = seri.validated_data['stage_name'])
            return Response({
                'id' : artist.id,
                'stage_name' : artist.stage_name,
                'social_link' : artist.social_link 
            }, status=status.HTTP_201_CREATED)
        
        return Response(seri.errors, status=status.HTTP_400_BAD_REQUEST)
