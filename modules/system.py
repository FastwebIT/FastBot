from telethon import events

def setup(client):
    @client.on(events.NewMessage(outgoing=True, pattern=r"\.del"))
    async def delete_single_message(event):
        if event.is_reply:
            reply_msg = await event.get_reply_message()
            await event.delete()
            await reply_msg.delete()
        else:
            await event.delete()

    @client.on(events.NewMessage(outgoing=True, pattern=r"\.react (.+)"))
    async def quick_reaction(event):
        emoji = event.pattern_match.group(1)
        if event.is_reply:
            reply_msg = await event.get_reply_message()
            await event.delete()
            await event.client.react(event.chat_id, reply_msg.id, emoji)
        else:
            await event.edit("⚠️ *Rispondi a un messaggio per lasciare una reazione!*")