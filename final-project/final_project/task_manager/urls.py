from rest_framework import routers

from .views.auth import AuthViewset
from .views.comments import CommentViewset
from .views.projects import ProjectViewset
from .views.tasks import TaskViewset
from .views.users import UserViewset

router = routers.DefaultRouter()

router.register('comment', CommentViewset, basename = 'comment')
router.register('project', ProjectViewset, basename = 'project')
router.register('task', TaskViewset, basename = 'task')
router.register('user', UserViewset, basename = 'user')
router.register('auth', AuthViewset, basename = 'auth')

router.urlpatterns = router.urls
