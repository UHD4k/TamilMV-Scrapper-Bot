from pyrogram import Client, __version__
import re, os, time
from datetime import datetime
from pytz import timezone
from pyrogram.raw.all import layer
from aiohttp import web
from route import web_server
import pyromod
import pyrogram.utils
from plugins.core.bypass_checker import app as Client2

pyrogram.utils.MIN_CHAT_ID = -999999999999
pyrogram.utils.MIN_CHANNEL_ID = -100999999999999

id_pattern = re.compile(r'^.\d+$') 

BOT_TOKEN = os.environ.get("TOKEN", "7713324413:AAGYzSbK5Z9KbhaJGiQdA7Rs-YaYLk4fNiU")
API_ID = int(os.environ.get("API_ID",11973721))
API_HASH = os.environ.get("API_HASH", "5264bf4663e9159565603522f58d3c18")
BOT_UPTIME  = time.time()
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001821439025"))
WEBHOOK = bool(os.environ.get("WEBHOOK", True))
ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '1391556668 1242556540').split()]
STRING_SESSION = os.environ.get("STRING_SESSION", "1BVtsOKEBu5Pf_Oesjuxt4TIzNijt1iMjJ8hEa3xtURQFrsd0GFYLhS_XFm2iJ61NfFeKR5icfMSu_SWH3eRvvdZ-X7IyOVFZuQ4sHKoiju_WXCH4uQqqd7vB7_9hGyMbDk7mUgjVKNkRg0trupt-5mu8pAeWAZ3US61kBnLKvsMYSjiaiL3uWI3UDfzyNQzFhf_hXWF_XskD0QrMPS87wEd85iNzXBgBE9Sae2haJ8YppGWxhcGtmJDSqHnDSlxh2dFLBZ1K_o7zxE6i1FrOaqEL_gKW87xqc2W43kCsUj-s9A9GyXdP7aUxu1Mku5j3GyMxEWS79Yku7AfxyeGUYhTw5dXGScE=")

class Bot(Client):

    def __init__(self):
        super().__init__(
            name="GTStarBot",
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            workers=200,
            plugins={"root": "plugins"},
        )

    async def start(self):
        await super().start()
        me = await self.get_me()
        self.mention = me.mention
        self.username = me.username  
        self.uptime = BOT_UPTIME          
        print(f"{me.first_name} is Started...✨️\nMade By :- https://t.me/Star_Bots_Tamil")
        if WEBHOOK:
            app = web.AppRunner(await web_server())
            await app.setup()       
            await web.TCPSite(app, "0.0.0.0", 8080).start()
        for id in ADMIN:
            try: await self.send_message(id, f"**__{me.first_name} is Started...✨️\nMade By :- [Star Bots Tamil](https://t.me/Star_Bots_Tamil)__**")                                
            except: pass
        if LOG_CHANNEL:
            try:
                curr = datetime.now(timezone("Asia/Kolkata"))
                date = curr.strftime('%d %B, %Y')
                time = curr.strftime('%I:%M:%S %p')
                await self.send_message(LOG_CHANNEL, f"**__{me.mention} is Restarted. !!**\n\n📅 Date :- `{date}`\n⏰ Time :- `{time}`\n🌐 TimeZone :- `Asia/Kolkata`\n\n🉐 Version :- `v{__version__} (Layer {layer})`</b>")                                
            except:
                print("Please Make This is Admin in Your Log Channel")

    async def stop(self, *args):
        await super().stop()      
        print("Bot Stopped... Bye")
       
if STRING_SESSION:
    apps = [Client2, Bot]
    for app in apps:
        app.start()
    idle()
    for app in apps:
        app.stop()
    
else:
    Bot().run()
