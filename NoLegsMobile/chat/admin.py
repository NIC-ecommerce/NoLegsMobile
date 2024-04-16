from django.contrib import admin
from .models import ChatRoom, Message ,ChatMember

# Регистрируем модели в административном интерфейсе
admin.site.register(ChatRoom)
admin.site.register(Message)
admin.site.register(ChatMember)
