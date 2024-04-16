import os
import django
import asyncio

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'NoLegsMobile.settings')
django.setup()
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from chat.routing import websocket_urlpatterns



application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    "websocket": URLRouter(websocket_urlpatterns)
})
