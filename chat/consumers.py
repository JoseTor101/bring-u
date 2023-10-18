import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from chat.models import Message, Chat
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from asgiref.sync import async_to_sync

class ChatSystem(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
    """async def connect(self):
        self.id_chat = self.scope["url_route"]["kwargs"]["id_chat"]
        self.group_name = f"chat_{self.id_chat}"

        await self.channel_layer.group_add(
            self.group_name, 
            self.channel_name)

        await self.accept()"""

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.group_name, self.channel_name)

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        username = text_data_json["user"]
        chat_id = self.id_chat

        await self.channel_layer.group_send(
            self.group_name,
            {
                "type": "chat_message",
                "user": username,
                "message": message,
                "chat_id": chat_id,
            },
        )

    async def chat_message(self, event):
        message = event["message"]
        username = event["user"]
        chat_id = event["chat_id"]

        # Uncomment this line to save the message to the database
        await self.save_message(username, message, chat_id)

    async def save_message(self, user, message, chat_id):
        print("IMPRIMAAAAAAAAAAAAAA")
        print(self, " ", self.user, " ", self.message, " ", self.id_chat)
        Message.objects.create(user=user, content=message, fk_id_chat=chat_id)
