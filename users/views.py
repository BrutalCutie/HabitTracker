from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from users.models import User
from users.permissions import IsSuperUser, IsAccountOwner
from users.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsSuperUser]

    def perform_create(self, serializer):
        user = serializer.save()
        user.set_password(user.password)
        user.save()

    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes = [AllowAny]

        elif self.action in ['patrial_update', 'update', 'retrieve']:
            self.permission_classes = [IsAccountOwner | IsSuperUser]

        return super().get_permissions()
