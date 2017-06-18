from channels import Group
from channels.message import Message
from channels.sessions import channel_session


# Connected to websocket.connect
@channel_session
def ws_connect(message: Message):
    # Accept connection
    message.reply_channel.send({'accept': True})

    # Work out room name from path (ignore slashes)
    room = message.content['path'].strip('/')

    # Save room in session and add us to the group
    message.channel_session['room'] = room

    # Add them to channel group
    Group(f'chat-{room}').add(message.reply_channel)


# Connected to websocket.receive
@channel_session
def ws_message(message: Message):
    Group(f'chat-{message.channel_session["room"]}').send({
        'text': f'[user] {message.content["text"]}',
    })


# Connected to websocket.disconnect
@channel_session
def ws_disconnect(message: Message):
    Group(f'chat-{message.channel_session["room"]}').discard(
        message.reply_channel)
