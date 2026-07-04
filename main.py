import asyncio
import os
import importlib
from telethon import TelegramClient

# Inserisci i tuoi dati reali presi da my.telegram.org
API_ID = 1234567         # Deve essere un numero INTERO (senza virgolette)
API_HASH = "la_tua_api_hash_qui"

client = TelegramClient("mio_account", API_ID, API_HASH)

def load_modules():
    print("Caricamento moduli in corso...")
    modules_dir = os.path.join(os.path.dirname(__file__), "modules")
    
    if not os.path.exists(modules_dir):
        print(f"⚠️ Errore: La cartella '{modules_dir}' non esiste!")
        return

    for file in os.listdir(modules_dir):
        if file.endswith(".py") and not file.startswith("__"):
            module_name = f"modules.{file[:-3]}"
            try:
                # Importa il modulo
                mod = importlib.import_module(module_name)
                
                # Se il modulo ha una funzione chiamata "setup", la eseguiamo passandogli il client
                if hasattr(mod, "setup"):
                    mod.setup(client)
                    print(f"✅ Modulo inizializzato: {file}")
                else:
                    print(f"⚠️ Modulo saltato (manca la funzione setup): {file}")
            except Exception as e:
                print(f"❌ Errore nel caricamento di {file}: {e}")

async def main():
    print("Userbot modulare in avvio...")
    await client.start()
    
    # Carichiamo e colleghiamo i moduli al client attivo
    load_modules()
    
    print("\n🚀 Userbot ONLINE! Prova i comandi nei Messaggi Salvati.")
    await client.run_until_disconnected()

if __name__ == "__main__":
    asyncio.run(main())