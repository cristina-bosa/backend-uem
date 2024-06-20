from http import HTTPStatus

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from task_manager.models import Users
from task_manager.models.comments import Comments
from task_manager.models.tasks import Tasks
from task_manager.serializers.comments import CommentSerializer
from task_manager.serializers.tasks import TaskSerializer
from task_manager.utils.send_notifications import TelegramBot


class TaskViewset(viewsets.ModelViewSet):
    # TODO: Un usuario puede eliminar una tarea a un proyecto ✅ -> envio de notificaciones ❌
    # TODO: Un usuario puede añadir una tarea a un proyecto ✅ -> envio de notificaciones ❌
    # TODO: Un usuario puede eliminar una tarea a un usuario ✅ -> envio de notificaciones ❌
    # TODO: Un usuario puede añadir una tarea a un usuario ✅ -> envio de notificaciones ❌
    # TODO: Un usuario puede cambiar el estado de una tarea ✅ -> envio de notificaciones ❌
    # TODO: Un usuario puede ver las tareas de un proyecto ✅ hecho en projects
    # TODO: Un usuario puede ver sus propias tareas ✅

    queryset = Tasks.objects.all()
    serializer_class = TaskSerializer

    def create(self, request, *args, **kwargs):
        try:
            serializer = self.serializer_class(data = request.data)
            if serializer.is_valid():
                serializer.save()
                users = Users.objects.filter(id__in = request.data['users'])
                TelegramBot().send_message(request.user, f'La tarea {serializer.data["name"]} se ha creado')
                for user in users:
                    TelegramBot().send_message(user, f'La tarea {serializer.data["name"]} se te ha añadido')
                return Response(serializer.data, status = HTTPStatus.CREATED)
            else:
                return Response(serializer.errors, status = HTTPStatus.BAD_REQUEST)
        except Exception as e:
            return Response(status = HTTPStatus.BAD_REQUEST)

    def delete(self, request, pk):
        try:
            task = self.queryset.get(pk = pk)
            task.delete()
            TelegramBot().send_message(request.user, f'La tarea {task.name} se eliminado')
            return Response(status = HTTPStatus.NO_CONTENT)
        except Tasks.DoesNotExist:
            return Response(status = HTTPStatus.NOT_FOUND)

    @action(detail = True, methods = ['put'], url_path = 'change-status', permission_classes = [IsAuthenticated])
    def change_status(self, request, pk):
        try:
            task = self.queryset.get(pk = pk)
            task.status = request.data['status']
            task.save()
            TelegramBot().send_message(request.user, f'La tarea {task.name} cambiado su estado a {task.status}')
            return Response({'message': 'Status changed successfully'}, status = HTTPStatus.ACCEPTED)
        except Tasks.DoesNotExist:
            return Response(status = HTTPStatus.NOT_FOUND)

    @action(detail = True, methods = ['put'], url_path = 'add-users-task', permission_classes = [IsAuthenticated])
    def add_user_task(self, request, pk):
        try:
            task = self.queryset.get(pk = pk)
            users = request.data['users']
            for user in users:
                task.users.add(user)
                TelegramBot().send_message(user, f'El usuario {request.user.username} te ha asignado la tarea {task.name}')
            return Response({'message': 'Users added successfully'}, status = HTTPStatus.ACCEPTED)
        except Tasks.DoesNotExist:
            return Response(status = HTTPStatus.NOT_FOUND)

    @action (detail = True, methods = ['delete'], url_path = 'delete-users-task', permission_classes = [
        IsAuthenticated])
    def delete_user_task(self, request, pk):
        try:
            task = self.queryset.get(pk = pk)
            users = Users.objects.filter(id__in = request.data['user'])
            for user in users:
                task.users.remove(user)
                TelegramBot().send_message(user, f'El usuario {request.user.username} te ha eliminado la tarea'
                                                 f' {task.name}')
            return Response({'message': 'Users removed successfully'}, status = HTTPStatus.ACCEPTED)
        except Tasks.DoesNotExist:
            return Response(status = HTTPStatus.NOT_FOUND)

    @action(detail = False, methods = ['get'], url_path ='me', permission_classes = [IsAuthenticated])
    def me(self, request):
        try:
            user_id = request.user.id
            tasks = self.queryset.filter(users = user_id)
            return Response(TaskSerializer(tasks, many = True).data)
        except Tasks.DoesNotExist:
            return Response(status = HTTPStatus.NOT_FOUND)

    @action(detail = True, methods = ['get'], url_path = 'comments', permission_classes = [IsAuthenticated])
    def get_comments_task(self, request, pk):
        try:
            task = self.queryset.get(pk = pk)
            comments = task.comments_set.all()
            serializer = CommentSerializer(comments, many = True)
            return Response(serializer.data)
        except Comments.DoesNotExist:
            return Response(status = HTTPStatus.NOT_FOUND)
