from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import chat.routing

application = ProtocolTypeRouter({
    #http views is added by default
    'websocket':
    AuthMiddlewareStack(URLRouter(chat.routing.websocket_urlpatterns))
})
