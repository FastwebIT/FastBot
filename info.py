from telethon import events

def setup(client):
    @client.on(events.NewMessage(outgoing=True, pattern=r"\.info"))
    async def info_handler(event):
        chat = await event.get_chat()
        chat_id = event.chat_id
        chat_type = type(chat).__name__
        
        text = f"ℹ️ **Info Chat:**\n\n🔹 **ID Chat:** `{chat_id}`\n🔹 **Tipo Chat:** `{chat_type}`"
        
        # Se la chat ha un titolo (gruppi/canali), lo aggiunge alla risposta
        if hasattr(chat, 'title'):
            text += f"\n🔹 **Titolo:** `{chat.title}`"
        # Se è una chat privata con un utente, mostra l'username se presente
        elif hasattr(chat, 'username') and chat.username:
            text += f"\n🔹 **Username:** @{chat.username}"
            
        await event.edit(text)