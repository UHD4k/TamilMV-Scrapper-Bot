from pyrogram import Client, idle
import os, time, asyncio, re
from plugins.core.bypass_checker import app as Client2
import pyrogram
pyrogram.utils.MIN_CHAT_ID = -999999999999
pyrogram.utils.MIN_CHANNEL_ID = -100999999999999

id_pattern = re.compile(r'^.\d+$')

BOT_TOKEN = os.environ.get("TOKEN", "7713324413:AAGYzSbK5Z9KbhaJGiQdA7Rs-YaYLk4fNiU")
API_ID = int(os.environ.get("API_ID",11973721))
API_HASH = os.environ.get("API_HASH", "5264bf4663e9159565603522f58d3c18")
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001821439025"))
STRING_SESSION = os.environ.get("STRING_SESSION", "1BVtsOKEBu5Pf_Oesjuxt4TIzNijt1iMjJ8hEa3xtURQFrsd0GFYLhS_XFm2iJ61NfFeKR5icfMSu_SWH3eRvvdZ-X7IyOVFZuQ4sHKoiju_WXCH4uQqqd7vB7_9hGyMbDk7mUgjVKNkRg0trupt-5mu8pAeWAZ3US61kBnLKvsMYSjiaiL3uWI3UDfzyNQzFhf_hXWF_XskD0QrMPS87wEd85iNzXBgBE9Sae2haJ8YppGWxhcGtmJDSqHnDSlxh2dFLBZ1K_o7zxE6i1FrOaqEL_gKW87xqc2W43kCsUj-s9A9GyXdP7aUxu1Mku5j3GyMxEWS79Yku7AfxyeGUYhTw5dXGScE=")

Bot = Client("1TamilMVScrapper", bot_token=BOT_TOKEN, api_id=API_ID, api_hash=API_HASH, plugins=dict(root='plugins'))

async def start(self):
    global True
    await super().start()
    print("Bot Started!")

    # Notify in log channels
    for chat in [LOG_CHANNEL, Config.TAMILMV_LOG, Config.TAMILBLAST_LOG, Config.GROUP_ID]:
        try:
            await self.send_message(chat, "Bot Started!")
            await Client2.send_message(chat, "Bot Started For Auto Leech")
        except Exception as e:
            print(f"Error sending start message to chat {chat}: {e}")

    # Start and manage Client2 and Bot concurrently using asyncio
    if STRING_SESSION:
        # Run Client2 and Bot in parallel
        tasks = [
            asyncio.create_task(Client2.start()), 
            asyncio.create_task(self.start())
        ]
        await asyncio.gather(*tasks)

    else:
        self.run()

    # Start the scraper loop
    while True:
        try:
            print("TamilMV RSS Feed Running...")
            await tamilmv_rss_feed(self)

            print("TamilBlasters RSS Feed Running...")
            await tamilblasters_rss_feed(self)

            print("TamilMV RSS Feed Running for Group...")
            await tamilmv_rss_feed_user(Client2)

            print("TamilBlasters RSS Feed Running for Group...")
            await tamilblasters_rss_feed_user(Client2)

            print("Sleeping for 5 minutes...")
            await asyncio.sleep(300)
        except Exception as e:
            print(f"Error in scraper loop: {e}")
            await self.send_message(LOG_CHANNEL, f"Error occurred: {str(e)}")
            await asyncio.sleep(60)

    print("Bot Stopped!")
    for chat in [LOG_CHANNEL]:
        try:
            await self.send_message(chat, "Bot Stopped!")
        except Exception as e:
            print(f"Error sending stop message to chat {chat}: {e}")
            
