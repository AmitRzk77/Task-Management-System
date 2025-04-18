from rest_framework.routers import DefaultRouter
from tasks.viewsets.tasks_viewsets import TaskViewSet

router = DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='tasks')

urlpatterns = router.urls
