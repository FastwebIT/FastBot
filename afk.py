import asyncio
from telethon import events

is_afk = False
afk_reason = ""

def setup(client):
    @client.on(events.NewMessage(outgoing=True, pattern=r"\.afk(?: (.+))?"))
    async def set_afk(event):
        global is_afk, afk_reason
        is_afk = True
        afk_reason = event.pattern_match.group(1) if event.pattern_match.group(1) else "Non specificato"
        await event.edit(f"💤 **Modalità AFK Attivata.**\n\n📝 **Motivo:** {afk_reason}")

    @client.on(events.NewMessage(incoming=True))
    async def check_mentions(event):
        global is_afk, afk_reason
        if not is_afk:
            return
        if event.is_private or event.mentioned:
            await event.reply(f"🤖 **Sono AFK al momento.**\n📝 **Motivo:** {afk_reason}")

    @client.on(events.NewMessage(outgoing=True))
    async def auto_disable_afk(event):
        global is_afk
        if is_afk and not event.text.startswith(".afk"):
            is_afk = False
            msg = await event.respond("🌅 **Sono tornato! Modalità AFK disattivata.**")
            await asyncio.sleep(3)
            await msg.delete()