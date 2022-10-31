from albums.models import Album
from .serializers import AlbumSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework import pagination
from django_filters import rest_framework as filters
from rest_framework import viewsets
from rest_framework import permissions


# Create your views here.

class AlbumFilters(filters.FilterSet):

    class Meta:
        model = Album
        fields = {
            'cost' : ['gte', 'lte'],
            'name' : ['icontains']
        }


class AlbumApi(viewsets.ModelViewSet):
    queryset = Album.objects.filter(is_approved_by_admin = True)
    serializer_class = AlbumSerializer
    filterset_class = AlbumFilters
    pagination_class = pagination.LimitOffsetPagination
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def create(self, request, *args, **kwargs):
        if not hasattr(request.user, 'artist'):
            return Response(status=status.HTTP_403_FORBIDDEN, data = {'status': status.HTTP_403_FORBIDDEN,'message':'this user is not an artist'})

        seri = AlbumSerializer(data = request.data)
        seri.is_valid(raise_exception=True)
        self.perform_create(seri)
        return Response(seri.data, status=status.HTTP_201_CREATED)

    def perform_create(self, serializer):
        serializer.save(artist = self.request.user.artist)
