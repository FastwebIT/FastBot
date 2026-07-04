from telethon import events

def setup(client):
    @client.on(events.NewMessage(outgoing=True, pattern=r"\.ping"))
    async def ping_handler(event):
        await event.edit("🏓 **Pong!**")