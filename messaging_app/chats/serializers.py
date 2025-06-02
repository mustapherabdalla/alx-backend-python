from rest_framework import serializers # type: ignore
from .models import *

class UserSerializer(serializers.ModelSerializer):
  first_name = serializers.CharField(source='first_name', max_length=200)
  last_name = serializers.CharField(source='last_name', max_length=200)
  email = serializers.CharField(source='email', max_length=200)
  phone_number = serializers.CharField(source='phone_number', max_length=200)

  class Meta:
    model = User
    fields = ['user_id', 'first_name', 'last_name', 'email', 'phone_number']
    read_only_fields= ['user_id']

  def validate_first_name(self, value):
    if len(value) < 0:
      raise serializers.ValidationError("First name cannot be empty!")

    elif len(value) < 2:
      raise serializers.ValidationError("First name must be long than two letter!")

    elif any(char.isDigit() for char in value):
      raise serializers.ValidationError("First name cannot contain number!")
    
    return value
  

  def validate_last_name(self, value):
    if len(value) < 0:
      raise serializers.ValidationError("Last name cannot be empty!")

    elif len(value) < 2:
      raise serializers.ValidationError("Last name must be long than two letter!")

    elif any(char.isDigit() for char in value):
      raise serializers.ValidationError("Last name cannot contain number!")
    
    return value
  

  def validate_email(self, value):
    if len(value) < 0:
      raise serializers.ValidationError("Email cannot be empty!")

    elif len(value) < 2:
      raise serializers.ValidationError("Email must be long than two letter!")

    
    for char in value:
      if char != '@':
        raise serializers.ValidationError("Email address must contain @")
      
      elif char != '.':
        raise serializers.ValidationError("Email address must contain .")
    
    return value
  

  def validate_phone_number(self, value):
    if len(value) < 0:
      raise serializers.ValidationError("Phone number cannot be empty!")

    elif len(value) < 10:
      raise serializers.ValidationError("Phone number must be long than ten digits!")

    elif not any(char.isDigit() for char in value):
      raise serializers.ValidationError("Phone number must contain digits only!")
    
    return value


class ConversationSerializer(serializers.ModelSerializer):
  participants = UserSerializer(many=True, read_only=True)
  conversation_object = serializers.SerializerMethodField()

  class Meta:
    model = Conversation
    fields = '__all__'

  def get_conversation_object(self, obj):
    if obj.participants.count() < 2:
      raise serializers.ValidationError("There should more than one participant in a conversation!")

    return obj

class MessageSerializer(serializers.ModelSerializer):
  sender = UserSerializer(read_only=True)
  receiver = UserSerializer(read_only=True)
  conversation = ConversationSerializer(read_only=True)

  message_object = serializers.SerializerMethodField()

  class Meta:
    model = Message
    fields = '__all__'


  def get_message_object(self, obj):
    if len(obj.message_body) == 0:
       raise serializers.ValidationError("Message body cannot be empty!!")

    return obj
