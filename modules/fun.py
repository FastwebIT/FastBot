import asyncio
from telethon import events

def setup(client):
    @client.on(events.NewMessage(outgoing=True, pattern=r"\.loading"))
    async def loading_animation(event):
        animation = [
            " Randall [□□□□□□□□□□] 0%",
            " Randall [■■□□□□□□□□] 20%",
            " Randall [■■■■□□□□□□] 40%",
            " Randall [■■■■■■□□□□] 60%",
            " Randall [■■■■■■■■□□] 80%",
            " Randall [■■■■■■■■■■] 100%",
            "🚀 **Processo Completato con Successo!**"
        ]
        for frame in animation:
            await event.edit(frame)
            await asyncio.sleep(0.4)