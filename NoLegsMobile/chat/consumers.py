# consumers.py
import json

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer

from chat.serializers import MessageSerializer
from .models  import Message,ChatRoom

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_id = self.scope["url_route"]["kwargs"]["room_id"]
        self.room_group_id = f"chat_{self.room_id}"

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_id, self.channel_name
        )
        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_id, self.channel_name
        )

    async def receive(self, text_data):
        data = json.loads(text_data)
        sender_type = data.get('sender_type')
        sender_id = data.get('sender_id')
        message_type = data.get('message_type')
        location = data.get('location')
        notification_text = data.get('notification_text')

        message = Message.objects.create(
            sender_type=sender_type,
            sender_id=sender_id,
            message_type=message_type,
            location=location,
            notification_text=notification_text
        )

        serializered_message = MessageSerializer(message).data

        await self.channel_layer.group_send(
            self.room_group_id,
            {
                'type': 'chat_message',
                'message': serializered_message


            }
        )

    async def chat_message(self, event):
        message = event.get('message')
        if message:
            await self.send(text_data=json.dumps(event['message']))

