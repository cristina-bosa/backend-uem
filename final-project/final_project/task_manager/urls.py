from rest_framework import routers

from .views.auth import AuthViewset
from .views.comments import CommentViewset
from .views.projects import ProjectViewset
from .views.tasks import TaskViewset

router = routers.DefaultRouter()

router.register('comment', CommentViewset, basename = 'comment')
router.register('projects', ProjectViewset, basename = 'project')
router.register('task', TaskViewset, basename = 'task')
router.register('auth', AuthViewset, basename = 'auth')

router.urlpatterns = router.urls
