from channels import Group
from channels.message import Message


# Connected to websocket.connect
def ws_add(message: Message):
    # Accept the incoming connection
    message.reply_channel.send({'accept': True})

    # Add them to channel group
    Group('chat').add(message.reply_channel)


# Connected to websocket.receive
def ws_message(message: Message):
    Group('chat').send({
        'text': f'[user] {message.content["text"]}',
    })


# Connected to websocket.disconnect
def ws_disconnect(message: Message):
    Group('chat').discard(message.reply_channel)
