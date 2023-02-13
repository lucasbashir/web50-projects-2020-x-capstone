from channels.generic.websocket import AsyncWebSocketConsumer
import json

class NewPostAlertConsumer(AsyncWebSocketConsumer):
    async def connect(self):
        await self.accept()
        await self.send(text_data=json.dumps({
            'message': 'Welcome to the New Post Alert Chanel'

        }))

    async def disconnect(self):
        pass

    async def receive(self, close_code):
        pass
    
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        await self.send(text_data=json.dumps({
            'message': message
        }))