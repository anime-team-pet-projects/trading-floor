from rest_framework.generics import CreateAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_204_NO_CONTENT

from api.v1.user.serializers import UserDetailSerializer, UserProfileSerializer
from apps.user.models import User


class SignUpAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer
    permission_classes = [AllowAny]


class MeAPIView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.filter(is_active=True)
    serializer_class = UserDetailSerializer
    permission_classes = [IsAuthenticated]

    def retrieve(self, request, *args, **kwargs):
        serializer = self.serializer_class(request.user, context={'request': request})

        return Response(serializer.data)

    def get_object(self):
        return self.request.user

    def delete(self, request, *args, **kwargs):
        request.user.is_active = False
        request.user.save()

        return Response(status=HTTP_204_NO_CONTENT)


class UserProfileAPIView(RetrieveAPIView):
    queryset = User.objects.filter(is_active=True)
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]
