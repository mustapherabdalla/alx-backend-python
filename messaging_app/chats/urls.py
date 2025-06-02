from django.urls import path, include   # type: ignore
from rest_framework.routers import DefaultRouter   # type: ignore
from .views import ConversationViewSet, MessageViewSet

router = DefaultRouter()
router.register(r"conversations", ConversationViewSet)
router.register(r"messages", MessageViewSet)

urlpatterns = [
  path('', include(router.urls)),
]
