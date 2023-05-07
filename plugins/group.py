from googletrans import Translator
from pyrogram import Client, filters
from helper.list import list
from helper.database import find_one

@Client.on_message(filters.group & filters.command(["translate"]))
async def left(client,message):
	if (message.reply_to_message):
		try:
			lgcd = message.text.split("/translate")
			lg_cd = lgcd[1].lower().replace(" ", "")
			tr_text = message.reply_to_message.text
			translator = Translator()
			translation = translator.translate(tr_text,dest = lg_cd)
			try:
				for i in list:
					if list[i]==translation.src:
						fromt = i
					if list[i] == translation.dest:
						to = i 
				await message.reply_text(f"**Translated From {fromt.capitalize()} To {to.capitalize()}\n\n```{translation.text}```\n\nJoin [Star Bots Tamil](https://t.me/Star_Bots_Tamil)**")
			except:
			   	await message.reply_text(f"**Translated From {translation.src} To {translation.dest}\n\n```{translation.text}```\n\nJoin [Star Bots Tamil](https://t.me/Star_Bots_Tamil)**")
      			
				
			
		except :
			print("error")
	else:
			 ms = await message.reply_text("**You Can Use This Command with Your Language by using Reply to Message\n\n Example :-** ```/translate Tamil```")
			 await ms.delete()
