from django.shortcuts import render # type: ignore
from rest_framework import generics # type: ignore
from .models import *
from .serializers import *

# Create your views here.
class ConversationListCreateAPIView(generics.ListCreateAPIView):
  queryset = Conversation.objects.all()
  serializer_class = ConversationSerializer


class MessageListCreateAPIView(generics.ListCreateAPIView):
  queryset = Message.objects.all()
  serializer_class = MessageSerializer

# Create your views here.
