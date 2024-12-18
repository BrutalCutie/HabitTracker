from django.urls import path
from rest_framework.routers import DefaultRouter

from tracker.apps import TrackerConfig
from tracker.views import HabitViewSet, PublishedHabitsListAPIView, PublishedHabitsRetrieveAPIView

app_name = TrackerConfig.name


router = DefaultRouter()
router.register(r'habits', HabitViewSet, basename='habit')

urlpatterns = [
    path('published-habits/', PublishedHabitsListAPIView.as_view(), name='published-habits'),
    path('published-habits/<int:pk>/', PublishedHabitsRetrieveAPIView.as_view(), name='published-habits-retrieve')
] + router.urls

