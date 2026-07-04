import asyncio
from telethon import events

def setup(client):
    @client.on(events.NewMessage(outgoing=True, pattern=r"\.hacker"))
    async def hacker_troll(event):
        await event.edit("📡 *Connessione al server della vittima...*")
        await asyncio.sleep(0.8)
        await event.edit("🔑 *Bypassing del firewall in corso... (WPA2)*")
        await asyncio.sleep(1)
        await event.edit("💉 *Iniezione SQL eseguita nel database centrale...*")
        await asyncio.sleep(0.8)
        await event.edit("📥 *Download dei dati sensibili completato.*")
        await asyncio.sleep(0.6)
        await event.edit("💻 **[SISTEMA MANOMESSO CON SUCCESSO]**")