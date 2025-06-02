from django.db import models # type: ignore
from django.contrib.auth.models import AbstractUser # type: ignore

# Create your models here.
class User(AbstractUser):
  phone_number = models.CharField(max_length=100)
  role = models.CharField(max_length=100)
  
class Conversation(models.Model):
  participants = models.ManyToManyField(User, related_name='conversations')
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  is_group = models.BooleanField(default=False)
  name = models.CharField(max_length=200, null=True, blank=True)

class Message(models.Model):
  conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE, related_name='messages')
  sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
  receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recived_messages')
  content = models.TimeField()
  sent_at = models.DateTimeField(auto_now_add=True)
  read = models.BooleanField(default=False)
  
