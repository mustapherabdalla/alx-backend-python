# chats/views.py
from rest_framework import viewsets, status, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .models import Conversation, Message
from .serializers import ConversationSerializer, MessageSerializer

class ConversationViewSet(viewsets.ModelViewSet):
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['participants']  # Filter by participant IDs
    search_fields = ['messages__content']  # Search message content

    def get_queryset(self):
        # Only show conversations where current user is a participant
        return self.queryset.filter(participants=self.request.user)

    @action(detail=True, methods=['post'], status_code=status.HTTP_201_CREATED)
    def send_message(self, request, pk=None):
        conversation = self.get_object()
        serializer = MessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(conversation=conversation, sender=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MessageViewSet(viewsets.ModelViewSet):
    serializer_class = MessageSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['conversation', 'sender', 'read']
    ordering_fields = ['timestamp']
    ordering = ['-timestamp']  # Default ordering: newest first

    def get_queryset(self):
        # Only show messages in conversations where user participates
        return Message.objects.filter(
            conversation__participants=self.request.user
        ).select_related('sender', 'conversation')

    def perform_create(self, serializer):
        # Auto-set sender to current user
        serializer.save(sender=self.request.user)
      
