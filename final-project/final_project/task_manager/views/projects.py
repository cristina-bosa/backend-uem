from http import HTTPStatus

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from task_manager.models.projects import Projects
from task_manager.serializers.projects import ProjectSerializer
from task_manager.serializers.tasks import TaskSerializer
from task_manager.utils.send_notifications import TelegramBot


class ProjectViewset(viewsets.ModelViewSet):
    # TODO: Un usuario puede añadir/eliminar un employee a un proyecto ✅ -> envio de notificaciones ✅
    # TODO: Un admin puede cambiar el estado del proyecto ✅ -> envio de notificaciones ✅
    # TODO: Un admin/employee puede ver las tareas de un proyecto ✅
    queryset = Projects.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        try:
            serializer = self.serializer_class(data = request.data)
            if serializer.is_valid():
                serializer.save()
                TelegramBot().send_message(request.user, f'El proyecto - {serializer.data["name"]} se ha creado')
                return Response(serializer.data, status = HTTPStatus.CREATED)
            else:
                return Response(status = HTTPStatus.BAD_REQUEST)
        except Exception as e:
            return Response(status = HTTPStatus.BAD_REQUEST)

    def delete(self, request, pk):
        try:
            project = self.queryset.get(pk = pk)
            project.delete()
            TelegramBot().send_message(request.user, f'El proyecto { project.name } se ha eliminado')
            return Response(status = HTTPStatus.NO_CONTENT)
        except Projects.DoesNotExist:
            return Response(status = HTTPStatus.NOT_FOUND)

    @action(detail = True, methods = ['put'], url_path = 'change-status', permission_classes = [IsAuthenticated])
    def change_status(self, request, pk):
        try:
            project = self.queryset.get(pk = pk)
            project.status = request.data['status']
            project.save()
            TelegramBot().send_message(request.user, f'El proyecto - {project.name}  ha cambiado su estado a {project.status}')
            return Response({'message': 'Status changed successfully'}, status = HTTPStatus.ACCEPTED)
        except Projects.DoesNotExist:
            return Response(status = HTTPStatus.NOT_FOUND)

    @action(detail = True, methods = ['post'], url_path = 'tasks', permission_classes = [IsAuthenticated])
    def get_tasks(self, pk):
        try:
            project = self.queryset.get(pk = pk)
            tasks = project.tasks_set.all() # la magia que hace django por debajo. te relaciona las tablas.
            serializer = TaskSerializer(tasks, many = True)
            return Response(serializer.data, status = HTTPStatus.OK)
        except Projects.DoesNotExist:
            return Response(status = HTTPStatus.NOT_FOUND)
