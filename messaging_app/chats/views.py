from django.shortcuts import render # type: ignore
from rest_framework import viewsets # type: ignore
from .models import *
from .serializers import *

# Create your views here.
class ConversationViewSet(viewsets.ModelViewSet):
  queryset = Conversation.objects.all()
  serializer_class = ConversationSerializer


class MessageViewSet(viewsets.ModelViewSet):
  queryset = Message.objects.all()
  serializer_class = MessageSerializer
