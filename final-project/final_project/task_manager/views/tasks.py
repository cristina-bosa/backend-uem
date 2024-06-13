from rest_framework import viewsets

from task_manager.models.tasks import Tasks
from task_manager.serializers.tasks import TaskSerializer


class TaskViewset(viewsets.ModelViewSet):
    # TODO: Un admin puede añadir/eliminar una tarea a un proyecto -> envio de notificaciones
    # TODO: Un admin puede añadir/eliminar una tarea a un employee -> envio de notificaciones
    # TODO: Usuario puede cambiar el estado de una tarea -> envio de notificaciones
    # TODO: Un usuario puede ver las tareas de un proyecto
    # TODO: Employee puede ver sus tareas

    queryset = Tasks.objects.all()
    serializer_class = TaskSerializer
