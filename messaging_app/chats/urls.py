# chats/urls.py
from django.urls import path, include   # type: ignore
from rest_framework import routers   # type: ignore
from .views import ConversationViewSet, MessageViewSet

# Create a router and register viewsets
router = routers.DefaultRouter()
router.register(r'conversations', ConversationViewSet)
router.register(r'messages', MessageViewSet)

urlpatterns = [
    path('', include(router.urls)),  # Include all router-generated URLs
]
