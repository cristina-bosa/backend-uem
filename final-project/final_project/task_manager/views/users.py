from rest_framework import viewsets

from task_manager.models import Users
from task_manager.serializers.users import UserSerializer


class UserViewset(viewsets.ModelViewSet):
    # TODO: Un admin puede añadir/eliminar un usuario(employee) -> envio de notificaciones
    # TODO: Update profile

    queryset = Users.objects.all()
    serializer_class = UserSerializer

