import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from chat.models import Message, Chat
from notifications.models import Notification  # Import your Notification model
from accounts.models import UserProfile
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from asgiref.sync import async_to_sync

class ChatSystem(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f"chat_{self.room_name}"

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name,
        )

        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        username = text_data_json['username']

        # Determine if it's a chat message or a notification
        if 'recipient' in text_data_json:
            recipient = text_data_json['recipient']

            # Create a new notification and save it
            notification = await database_sync_to_async(Notification.objects.create)(
                recipient=recipient,
                content=message,
            )

            # Notify the recipient through WebSocket
            await self.channel_layer.group_send(
                f"chat_{recipient}",
                {
                    'type': 'notification',
                    'message': message,
                    'sender': username,
                }
            )
        else:
            # It's a chat message
            chat = await database_sync_to_async(Chat.objects.get)(id_chat=self.room_name)
            user_sender = await database_sync_to_async(UserProfile.objects.get)(username=username)

            # Create the Message object and associate it with the chat
            await database_sync_to_async(Message.objects.create)(
                sender=user_sender,
                content=message,
                fk_id_chat=chat
            )

            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'chat_message',
                    'message': message,
                    'username': username,
                }
            )

    async def notification(self, event):
        message = event['message']
        sender = event['sender']

        await self.send(
            text_data=json.dumps({
                'notification': message,
                'sender': sender,
            })
        )

    async def chat_message(self, event):
        message = event['message']
        username = event['username']

        await self.send(
            text_data=json.dumps({
                'message': message,
                'username': username,
            })
        )
