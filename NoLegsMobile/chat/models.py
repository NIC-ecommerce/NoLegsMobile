from django.db import models
from django.conf import settings
# Create your models here.
from users.models import CustomUser



class ChatRoom(models.Model):
    members = models.ManyToManyField(settings.AUTH_USER_MODEL, through='ChatMember')
    start_time = models.DateTimeField(auto_now_add=True)

class ChatMember(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    chat_room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE)


class Message(models.Model):
    SENDER_CHOICES = [
        ('Driver', 'Driver'),
        ('Passenger', 'Passenger'),
    ]
    MESSAGE_TYPE_CHOICES = [
        ('Location', 'Location'),
        ('Notification', 'Notification'),
    ]

    sender_type = models.CharField(max_length=10, choices=SENDER_CHOICES)
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    message_type = models.CharField(max_length=12, choices=MESSAGE_TYPE_CHOICES)
    location =models.CharField(max_length=30, null=True, blank=True)
    notification_text = models.TextField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.sender} - {self.message_type}'

    class Meta:
        ordering = ['-timestamp']