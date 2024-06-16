from http import HTTPStatus

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from task_manager.models.comments import Comments
from task_manager.serializers.comments import CommentSerializer
from ..utils.send_notifications import TelegramBot


class CommentViewset(viewsets.ModelViewSet):
    # TODO: Un usuario puede añadir un comentario a una tarea ✅ -> envio de notificaciones ✅
    # TODO: Un usuario puede ver los comentarios de una tarea ✅
    queryset = Comments.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        try:
            serializer = self.serializer_class(data = request.data)
            if serializer.is_valid():
                serializer.save()
                TelegramBot().send_message(request.user, f'El comentario {serializer.data["comment"]} se ha creado')
                return Response(serializer.data, status = HTTPStatus.CREATED)
            else:
                return Response(serializer.errors, status = HTTPStatus.BAD_REQUEST)
        except Exception as e:
            return Response(status = HTTPStatus.BAD_REQUEST)
