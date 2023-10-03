## Changes made

### Installed apps:

- 'channels': pip install channels
- 'daphne': pip install daphne 
- Modify channels install: python -m pip install -U channels["daphne"].

It's crucial to add this installed products in the settings files -> "INSTALLED_APPS"

### Files added

-'consumers.py': Handle of the websocket request 
-'routing.py': redirecting request to a proper route

### Other changes

- Changes in settings.py: 
ASGI_APPLICATION = "chat.routing.application" 

#Change'BACKEND' InMemoryChannel when creating a production version
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': "channels.layers.InMemoryChannelLayer"
        }
    }

### Start ASGI server

daphne config.asgi:application