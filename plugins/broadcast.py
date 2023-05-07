from pyrogram import Client ,filters
import os
from helper.database import getid, full_userbase
ADMIN = int(os.environ.get("ADMIN", 1391556668))


@Client.on_message(filters.private & filters.user(ADMIN) & filters.command(["broadcast"]))
async def broadcast(bot, message):
 if (message.reply_to_message):
   ms = await message.reply_text("**Geting All IDs From Database...**")
   ids = getid()
   tot = len(ids)
   await ms.edit(f"**Completed Broadcast 💌\n Sending Message To {tot} Users**")
   for id in ids:
     try:
     	await message.reply_to_message.copy(id)
     except:
     	pass

@Client.on_message(filters.private & filters.user(ADMIN) & filters.command(["stats"]))
async def stats(bot, message):
   ms = await message.reply_text("**Geting All Users 📊 Count From Database...**")
   total = len(ids)
   ids = getid()
   await ms.edit(f"**Total Users 📊 :- {total} Users**")
   for id in ids:

     	pass

@Client.on_message(filters.command('users') & filters.private & filters.user(ADMIN))
async def get_users(client, message):
    msg = await client.send_message(chat_id=message.chat.id, text=f"**Processing**")
    users = full_userbase()
    await msg.edit(f"**{len(users)} users are using this bot**")
