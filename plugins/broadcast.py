from pyrogram import Client ,filters
import os
from helper.database import getid, db
ADMIN = int(os.environ.get("ADMIN", 1391556668))

@Client.on_message(filters.private & filters.user(ADMIN) & filters.command(["broadcast"]))
async def broadcast(bot, message):
 if (message.reply_to_message):
   ms = await message.reply_text("**Geting All IDs From Database...**")
   ids = getid()
   tot = len(ids)
   await ms.edit(f"**Broadcast 💌 Completed\nSending Message To {tot} Users**")
   for id in ids:
     try:
     	await message.reply_to_message.copy(id)
     except:
     	pass

@Client.on_message(filters.command('stats') & filters.private & filters.user(ADMIN))
async def get_users(client, message):
    msg = await client.send_message(chat_id=message.chat.id, text=f"**Geting All Users 📊 Count From Database...**")
    total_users = await db.total_users_count()
    await msg.edit(f"**Total Users 📊 :- {len(total_users)} Users**")
