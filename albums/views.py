from albums.models import Album
from .serializers import AlbumSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework import pagination

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
