from rest_framework import viewsets

from task_manager.models.comments import Comments
from task_manager.serializers.comments import CommentSerializer


class CommentViewset(viewsets.ModelViewSet):
    # TODO: Un usuario puede añadir un comentario a una tarea -> envio de notificaciones
    # TODO: Un usuario puede ver los comentarios de una tarea
    queryset = Comments.objects.all()
    serializer_class = CommentSerializer
