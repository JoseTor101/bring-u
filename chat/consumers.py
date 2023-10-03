import json
from channels.generic.websocket import AsyncWebsocketConsumer

class ChatSystem(AsyncWebsocketConsumer):
    async def connect(self):
        self.id_chat = self.scope["url_route"]["kwargs"]["id_chat"]
        self.group_name = f"chat_{self.chat_id}"

        await self.channel_layer.group_add(self.group_name, self.channel_name)

        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.group_name, self.channel_name)

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        username = text_data_json["username"]

        await self.channel_layer.group_send(
            self.group_name,
            {
                "type": "chatbox_message",
                "message": message,
                "username": username,
                "chat_id": self.chat_id,
            },
        )

    async def chatbox_message(self, event):
        message = event["message"]
        username = event["username"]
        chat_id = event["chat_id"]

        await self.send(
            text_data=json.dumps(
                {
                    "message": message,
                    "username": username,
                    "chat_id": chat_id,
                }
            )
        )
