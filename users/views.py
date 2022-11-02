from rest_framework import permissions, viewsets

from .models import User
from .permissions import IsTheCurrentUser
from .serializers import UserSerializer


class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsTheCurrentUser]
