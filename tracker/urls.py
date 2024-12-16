from rest_framework.routers import DefaultRouter

from tracker.apps import TrackerConfig
from tracker.views import HabitViewSet

app_name = TrackerConfig.name


router = DefaultRouter()
router.register(r'habits', HabitViewSet, basename='habit')

urlpatterns = [] + router.urls

