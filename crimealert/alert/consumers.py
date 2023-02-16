from channels.generic.websocket import WebsocketConsumer
import json
from asgiref.sync import async_to_sync


from channels.generic.websocket import WebsocketConsumer
import json

class NotificationConsumer(WebsocketConsumer):
    def connect(self):
        self.group_name = "notification"
        async_to_sync(self.channel_layer.group_add)(self.group_name, self.channel_name)
        self.accept()

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(self.group_name, self.channel_name)

    def send_notification(self, event):
        message = event['message']
        self.send(text_data=json.dumps({'message': message}))
