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


class AlbumApiManuaFiltering(viewsets.ModelViewSet):
    queryset = Album.objects.filter(is_approved_by_admin = True)
    serializer_class = AlbumSerializer
    pagination_class = pagination.LimitOffsetPagination

    def list(self, request, *args, **kwargs):
        params = request.query_params
        gte = 0
        lte = 999999999999
        icontains = ""
        if 'cost__gte' in params:
            if params['cost__gte']:
                try:
                    data = int(params['cost__gte'])
                    gte = data
                except:
                    return Response(data = {
                        "cost__gte": [ "Enter a number."],
                    }, status=status.HTTP_400_BAD_REQUEST)

        if 'cost__lte' in params:
            if params['cost__lte']:
                try:
                    data = int(params['cost__lte'])
                    lte = data
                except:
                    return Response(data = {
                        "cost__lte": [ "Enter a number."],
                    }, status=status.HTTP_400_BAD_REQUEST)
        
        if 'name__icontains' in params:
            if params['name__icontains']:
                icontains = params['name__icontains']

        data = Album.objects.filter(cost__gte = gte, cost__lte = lte, name__icontains = icontains, is_approved_by_admin = True)
        seri = AlbumSerializer(data, many = True)

        if 'limit' not in params:
            return Response(seri.data)
        return self.get_paginated_response(self.paginate_queryset(seri.data))
