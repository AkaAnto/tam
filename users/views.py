from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response

from users.models import User
from users.serializers import UserSerializer, UserCreateSerializer, UserUpdateSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing users.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return UserSerializer
        if self.action in ['create']:
            return UserCreateSerializer
        if self.action in ['partial_update', 'update']:
            return UserUpdateSerializer
        return UserSerializer
