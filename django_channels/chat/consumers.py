from channels.handler import AsgiHandler
from channels.message import Message
from django.http import HttpResponse


def http_consumer(message: Message):
    response = HttpResponse(
        f'Hello, World! You asked for ${message.content["path"]}')

    for chunk in AsgiHandler.encode_response(response):
        message.reply_channel.send(chunk)
