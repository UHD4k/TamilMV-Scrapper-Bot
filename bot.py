from pyrogram import Client
import os

TOKEN = os.environ.get("TOKEN", "6043919342:AAGVl9ktA1YDKYvVKu-6xycVX7-9Fg69ZbU")

API_ID = int(os.environ.get("API_ID",11973721))

API_HASH = os.environ.get("API_HASH", "5264bf4663e9159565603522f58d3c18")

FORCE_SUB   = os.environ.get("FORCE_SUB", "Star_Bots_Tamil") 

if __name__ == "__main__" :
    plugins = dict(
        root="plugins"
    )
    app = Client(
        "GTBot",
        bot_token=TOKEN,
        api_hash=API_HASH,
        api_id=API_ID,
        plugins=plugins
    )
    app.run()
