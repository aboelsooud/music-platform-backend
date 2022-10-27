from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.auth import AuthToken
from users.models import User


class LoginApiView(ListCreateAPIView):
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
