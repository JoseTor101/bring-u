from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import re_path
from . import consumers

# URLs that handle the WebSocket connection are placed here.
websocket_urlpatterns=[
                    re_path(
                       r"ws/chat/<int:id_chat>/$", consumers.ChatSystem.as_asgi()
                    ),
                ]


application = ProtocolTypeRouter( 
    {
        "websocket": AuthMiddlewareStack(
            URLRouter(
               websocket_urlpatterns
            )
        ),
    }
)