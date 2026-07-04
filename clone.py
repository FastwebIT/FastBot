import os
from telethon import events
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.functions.account import UpdateProfileRequest
from telethon.tl.functions.photos import UploadProfilePhotoRequest, DeletePhotosRequest

# Variabili di stato globali per salvare i tuoi dati originali
saved_first_name = ""
saved_last_name = ""
saved_about = ""

def setup(client):
    @client.on(events.NewMessage(outgoing=True, pattern=r"\.clone"))
    async def clone_user(event):
        global saved_first_name, saved_last_name, saved_about
        if not event.is_reply:
            await event.edit("⚠️ **Rispondi al messaggio di un utente per clonarlo!**")
            return
            
        await event.edit("👥 **Clonazione in corso...**")
        reply_msg = await event.get_reply_message()
        user = await event.client.get_entity(reply_msg.sender_id)
        
        # 1. Salva i tuoi dati reali prima di sovrascriverli (solo al primo clone)
        me = await event.client.get_me()
        me_full = await event.client(GetFullUserRequest(me.id))
        if not saved_first_name:
            saved_first_name = me.first_name or ""
            saved_last_name = me.last_name or ""
            saved_about = me_full.full_user.about or ""

        # 2. Ottieni i dettagli della vittima
        full_victim = await event.client(GetFullUserRequest(user.id))
        victim_bio = full_victim.full_user.about or ""
        
        # 3. Scarica e imposta la foto profilo
        photo = await event.client.download_profile_photo(user.id, download_big=True)
        if photo:
            file = await event.client.upload_file(photo)
            await event.client(UploadProfilePhotoRequest(file=file))
            if os.path.exists(photo):
                os.remove(photo)
                
        # 4. Aggiorna nome, cognome e biografia
        await event.client(UpdateProfileRequest(
            first_name=user.first_name or "",
            last_name=user.last_name or "",
            about=victim_bio
        ))
        await event.edit(f"🎭 **Identità clonata con successo da {user.first_name}!**")

    @client.on(events.NewMessage(outgoing=True, pattern=r"\.revert"))
    async def revert_profile(event):
        global saved_first_name, saved_last_name, saved_about
        if not saved_first_name:
            await event.edit("⚠️ **Non hai un profilo clonato da ripristinare.**")
            return
            
        await event.edit("🔄 **Ripristino del profilo originale...**")
        
        # Ripristina i dati testuali originali
        await event.client(UpdateProfileRequest(
            first_name=saved_first_name,
            last_name=saved_last_name,
            about=saved_about
        ))
        
        # Elimina la foto profilo del clone (l'ultima inserita)
        my_photos = await event.client.get_profile_photos("me")
        if my_photos:
            await event.client(DeletePhotosRequest(id=[my_photos[0]]))
            
        saved_first_name = ""  # Reset dello stato
        await event.edit("🌅 **Profilo originale ripristinato correttamente!**")