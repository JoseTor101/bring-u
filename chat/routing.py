from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from django.urls import re_path
from . import consumers



websocket_urlpatterns = [
    re_path(r'ws/chat/(?P<room_name>\w+)', consumers.ChatSystem.as_asgi())
]

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(websocket_urlpatterns)),
})