from channels.message import Message


def ws_message(message: Message):
    # ASGI WebSocket packet-received and send-packet message types
    # both have a "text" key for their textual data
    message.reply_channel.send({
        'text': message.content['text'],
    })
