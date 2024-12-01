import os, re
import time
from datetime import datetime
from pytz import timezone
from pyrogram import Client, __version__, enums
from aiohttp import web
from route import web_server

id_pattern = re.compile(r'^.\d+$')

BOT_TOKEN = os.environ.get("TOKEN", "YOUR_BOT_TOKEN")
API_ID = int(os.environ.get("API_ID", 11973721))
API_HASH = os.environ.get("API_HASH", "YOUR_API_HASH")
BOT_UPTIME = time.time()
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001821439025"))
WEBHOOK = bool(os.environ.get("WEBHOOK", True))
ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '1391556668').split()]

USER_SESSION_STRING = os.environ.get("USER_SESSION_STRING", "BQGC3RAANsUaEkcicYxlinT7b-sZqSEmmB3k0U5ejPI11DfFNZWgw95JzOZzClAtOggpEERj6Uw7_Vc4QfYaOZEm9YovvszyJzdZOyrkhgYbE2W4LhtoGkIxh184OswP_atDNQIXEDPzV_8mYtc-9JlilUumlfIDpd-YwSRWYPefy2Yvdvs00q7b5UuMPlVG_psmZWr7Plwp2Z3jscZ6ZoltifWu4MbIvODdxvMMTOjRUNOLHgnlGxanFAiBQn0vD7e8rceLlGWXZ9nKvlQitBvIB4vbUBOIiAglexGoRJZxG0z1dSSBdRiO5jp7QG0vOiNcT-Y7JNaNi2MxwTWIjK6za76X7AAAAABS8Xg8AA")

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
        self.user_client = None
        if len(USER_SESSION_STRING) != 0:
            try:
                # Initialize the user client with the provided session string
                self.user_client = Client(
                    "user_client",
                    api_id=API_ID,
                    api_hash=API_HASH,
                    session_string=USER_SESSION_STRING,
                    workers=1000,
                    parse_mode=enums.ParseMode.HTML,
                    no_updates=True,
                )
                print("User client initialized successfully.")
            except Exception as e:
                print(f"Failed to initialize user client from USER_SESSION_STRING: {e}")
                self.user_client = None
        else:
            print("USER_SESSION_STRING is empty, skipping user client initialization.")

    async def start(self):
        # Start the bot client
        await super().start()
        # If user client is initialized, start it
        if self.user_client:
            await self.user_client.start()
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
            try:
                await self.send_message(id, f"**__{me.first_name} is Started...✨️\nMade By :- [Star Bots Tamil](https://t.me/Star_Bots_Tamil)__**")                                
            except: 
                pass
        if LOG_CHANNEL:
            try:
                curr = datetime.now(timezone("Asia/Kolkata"))
                date = curr.strftime('%d %B, %Y')
                time = curr.strftime('%I:%M:%S %p')
                await self.send_message(LOG_CHANNEL, f"**__{me.mention} is Restarted. !!**\n\n📅 Date :- `{date}`\n⏰ Time :- `{time}`\n🌐 TimeZone :- `Asia/Kolkata`\n\n🉐 Version :- `v{__version__} (Layer {layer})`</b>")                                
            except:
                print("Please Make This Bot Admin in Your Log Channel")

    async def stop(self, *args):
        # Ensure that we are running in the correct event loop and avoid closing it prematurely
        try:
            if self.user_client:
                await self.user_client.stop()
            await super().stop()  # Stop the bot client
            print("Bot and user client stopped. Goodbye!")
        except Exception as e:
            print(f"Error during stop: {e}")

    async def close(self):
        # Custom close function to handle manual closing of event loop, if needed
        if self.user_client:
            await self.user_client.stop()
        await super().close()

if __name__ == "__main__":
    bot = Bot()
    bot.run()
    
