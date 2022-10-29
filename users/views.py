from .models import User
from rest_framework import permissions
from .permissions import IsTheCurrentUser
from rest_framework import viewsets
from .serializers import UserSerializer

class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsTheCurrentUser]
