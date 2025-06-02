from rest_framework import serializers # type: ignore
from .models import *

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ['user_id', 'first_name', 'last_name', 'email', 'phone_number']
    read_only_fields= ['user_id']

class ConversationSerializer(serializers.ModelSerializer):
  participants = UserSerializer(many=True, read_only=True)

  class Meta:
    model = Conversation
    fields = '__all__'

class MessageSerializer(serializers.ModelSerializer):
  sender = UserSerializer(read_only=True)
  receiver = UserSerializer(read_only=True)
  conversation = ConversationSerializer(read_only=True)

  class Meta:
    model = Message
    fields = '__all__'