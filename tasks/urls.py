from rest_framework import routers
from tasks.views import TaskViewSet

router = routers.DefaultRouter()

router.register(r'api/tasks', TaskViewSet, 'tasks')

urlpatterns = router.urls
