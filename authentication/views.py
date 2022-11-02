from knox.auth import AuthToken
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from users.models import User

from .serializers import UserModelSerializer, UserRegiserSerializer


class LoginApiView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = AuthTokenSerializer

    def create(self, request, *args, **kwargs):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        _, token = AuthToken.objects.create(user)

        return Response({
            "token" : token,
            "user" : {
                "id" : user.id,
                "username" : user.username,
                "email" : user.email,
                "bio" : user.bio
            }
        })

class RegisterApiView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer

    def create(self, request, *args, **kwargs):
        serializer = UserRegiserSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        
        model_serializer = UserModelSerializer(data = serializer.data)
        model_serializer.is_valid(raise_exception=True)
        user = User.objects.create_user(username = serializer.validated_data['username'], email = serializer.validated_data['email'], password = serializer.validated_data['password'])
        _, token = AuthToken.objects.create(user)
        
        return Response({
            "token" : token,
            "user" : {
                "id" : user.id,
                "username" : user.username,
                "email" : user.email,
                "bio" : user.bio
            }
        })
