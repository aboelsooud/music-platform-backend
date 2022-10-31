from albums.models import Album
from .serializers import AlbumSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework import pagination
from dateutil.parser import parse

# Create your views here.


class AlbumApi(GenericAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    pagination_class = pagination.LimitOffsetPagination
    
    def get(self, request):
        data = Album.objects.filter(is_approved_by_admin=True)
        serializer = AlbumSerializer(data, many=True)
        if 'limit' not in request.query_params:
            return Response(serializer.data)
        return self.get_paginated_response(self.paginate_queryset(serializer.data))

    def post(self, request):
        if not request.user.is_authenticated:
            return Response(status=status.HTTP_403_FORBIDDEN, data = {'status': status.HTTP_403_FORBIDDEN,'message':'this user is not authenticated'})
        
        if not hasattr(request.user, 'artist'):
            return Response(status=status.HTTP_403_FORBIDDEN, data = {'status': status.HTTP_403_FORBIDDEN,'message':'this user is not an artist'})

        seri = AlbumSerializer(data = request.data)
        seri.is_valid(raise_exception=True)

        album = Album.objects.create(name = seri.validated_data['name'], release_date = seri.validated_data['release_date'], cost = seri.validated_data['cost'], artist = request.user.artist)
        
        response = AlbumSerializer(album)

        return Response(response.data)
