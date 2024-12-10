# Copyright 2024-present, Author: MrTamilKiD

import time
from typing import Union
from pyrogram import Client as pyClient
from pyrogram.storage import Storage
from config import Config, LOGGER
from plugins.core.bypass_checker import tamilmv_rss_feed, tamilblasters_rss_feed, tamilmv_rss_feed_user, tamilblasters_rss_feed_user
from plugins.core.bypass_checker import app as Client2  # Import Client2

class Client(pyClient):
    """ Custom Bot Class """

    def __init__(self, session_name: Union[str, Storage] = "TamilMVAutoRss-Bot"):
        super().__init__(
            session_name,
            api_id=Config.API_ID,
            api_hash=Config.API_HASH,
            bot_token=Config.BOT_TOKEN,
            plugins=dict(
                root="MrTamilKiD/plugins"
            )
        )

    async def start(self):
        await super().start()
        LOGGER.info("Bot Started!")
        
        # Notify in log channels
        for chat in Config.TAMILMV_LOG, Config.TAMILBLAST_LOG, Config.GROUP_ID:
            await self.send_message(chat, "Bot Started!")
        
        # Start Client2
        await Client2.start()
        
        # Send message to group_id using Client2
        await Client2.send_message(Config.GROUP_ID, "Bot Started For Auto Leech")

        # Start the scraper loop
        while True:
            print("TamilMV RSS Feed Running...")
            await tamilmv_rss_feed(self)

            print("TamilBlasters RSS Feed Running...")
            await tamilblasters_rss_feed(self)

            # Send message to GROUP_ID using Client2
            print("TamilMV RSS Feed Sending update to group...")
            await tamilmv_rss_feed_user(Client2)
            
            print("Tamilblasters RSS Feed Sending update to group...")
            await tamilblasters_rss_feed_user(Client2)

            print("Sleeping for 5 minutes...")
            time.sleep(300)

    async def stop(self, *args):
        await super().stop()
        LOGGER.info("Bot Stopped!")

        # Stop Client2
        await Client2.stop()
        
