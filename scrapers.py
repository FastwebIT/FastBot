from telethon import events

def setup(client):
    @client.on(events.NewMessage(outgoing=True, pattern=r"\.id"))
    async def get_ids(event):
        chat_id = event.chat_id
        text = f"🆔 **Dettagli ID:**\n\n🔹 **Questa Chat:** `{chat_id}`"
        if event.is_reply:
            reply_msg = await event.get_reply_message()
            text += f"\n👤 **Utente replicato:** `{reply_msg.sender_id}`"
            text += f"\n✉️ **Questo Messaggio:** `{reply_msg.id}`"
        await event.edit(text)