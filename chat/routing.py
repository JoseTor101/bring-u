from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import re_path
from chat import consumers


application = ProtocolTypeRouter({
    "websocket": URLRouter([
        re_path(r"ws/chat/(?P<id_chat>\d+)/$", consumers.ChatSystem.as_asgi())
    ]),
})



"""websocket_urlpatterns=[
                    re_path(
                       r"ws/chat/<int:id_chat>/$", consumers.ChatSystem.as_asgi()
                    ),
                ]"""

"""
application = ProtocolTypeRouter( 
    {
        "websocket": AuthMiddlewareStack(
            URLRouter(
               websocket_urlpatterns
            )
        ),
    }
)"""

