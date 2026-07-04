import asyncio
from telethon import events
from telethon.tl.functions.messages import SetTypingRequest
from telethon.tl.types import SendMessageRecordVideoAction, SendMessageUploadAudioAction

def setup(client):
    @client.on(events.NewMessage(outgoing=True, pattern=r"\.type (.+)"))
    async def typewriter_effect(event):
        text = event.pattern_match.group(1)
        current_text = ""
        for char in text:
            current_text += char
            if char != " ":
                await event.edit(f"{current_text} ▒")
                await asyncio.sleep(0.2)
        await event.edit(text)

    @client.on(events.NewMessage(outgoing=True, pattern=r"\.scam (vocale|video)"))
    async def fake_action(event):
        action_type = event.pattern_match.group(1)
        await event.delete()
        action = SendMessageUploadAudioAction() if action_type == "vocale" else SendMessageRecordVideoAction()
        for _ in range(2):
            await event.client(SetTypingRequest(peer=event.chat_id, action=action))
            await asyncio.sleep(4)