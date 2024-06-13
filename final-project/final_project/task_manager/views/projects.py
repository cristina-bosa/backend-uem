from rest_framework import viewsets
from rest_framework.response import Response

from task_manager.models.projects import Projects
from task_manager.serializers.projects import ProjectSerializer


class ProjectViewset(viewsets.ModelViewSet):
    # TODO: Un usuario puede añadir/eliminar un employee a un proyecto -> envio de notificaciones
    # TODO: Un admin puede cambiar el estado del proyecto -> envio de notificaciones
    # TODO: Un admin/employee puede ver las tareas de un proyecto
    queryset = Projects.objects.all()
    serializer_class = ProjectSerializer
