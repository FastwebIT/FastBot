from telethon import events

def setup(client):
    @client.on(events.NewMessage(outgoing=True, pattern=r"\.purge(?: (\d+))?"))
    async def purge_handler(event):
        if event.is_reply:
            msg_input = event.pattern_match.group(1)
            count = int(msg_input) if msg_input else 10
            reply_msg = await event.get_reply_message()
            messages = await event.client.get_messages(
                event.chat_id, 
                limit=count, 
                min_id=reply_msg.id - 1
            )
            await event.client.delete_messages(event.chat_id, messages)
        else:
            count = int(event.pattern_match.group(1)) if event.pattern_match.group(1) else 5
            messages = await event.client.get_messages(event.chat_id, limit=count)
            await event.client.delete_messages(event.chat_id, messages)