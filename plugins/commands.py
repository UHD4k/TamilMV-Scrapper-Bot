from pyrogram import Client, filters, enums
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup
)
from pyrogram.types import InlineQuery

@Client.on_message(filters.private & filters.command(['start']))
async def start(query: InlineQuery, message):
          await message.reply_text(text =f"<b>Hello 👋🏻 {message.from_user.first_name} ❤️\n\nI'm Star Bots Official Google Translator Bot. I Can Translate any Language to You Selected Language. You Can Set Your Language Permanently.\n\nTo know How to Use me check /help.\n\nI'll Work in Groups and Also Inline Anywhere.</b>",reply_to_message_id = message.id, disable_web_page_preview=True, parse_mode=enums.ParseMode.HTML, reply_markup=InlineKeyboardMarkup(            [                [                    InlineKeyboardButton("🤖 Bot Channel" ,url="https://t.me/Star_Bots_Tamil"),InlineKeyboardButton("Go Inline Here",switch_inline_query_current_chat='')],                 [InlineKeyboardButton("🎥 Movie Updates", url="https://t.me/Star_Moviess_Tamil"),InlineKeyboardButton("👥 Support Group",url = "https://t.me/Star_Bots_Tamil_Support") ]           ]        ) )
  
@Client.on_message(filters.private & filters.command(['help']))
async def help(client, message):
          await message.reply_text(text =f"<b>Hey 👋🏻 {message.from_user.first_name} Follow These Steps :-\n\n● Send /set language_name\n● Send /unset for Unsetting Current Default Language\n● Send /list for Languages List\n● Just Send a Text for Translation\n● Reply with Any Text With /translate language_name (Support Only Groups)\n● /text2speech - Reply with Text to Get Audio Speech 💬\n\nAvailable Commands\n\n● /start - Check if 😊 I'm Alive\n● /help - How to Use❓\n● /about - to Know About Me 😌\n\nMade by <a href=https://t.me/Star_Bots_Tamil><b></b>Star Bots Tamil</a></b>",reply_to_message_id = message.id , disable_web_page_preview=True, parse_mode=enums.ParseMode.HTML, reply_markup=InlineKeyboardMarkup(            [                [                    InlineKeyboardButton("🤖 Bot Channel" ,url="https://t.me/Star_Bots_Tamil") ],                 [InlineKeyboardButton("🎥 Movie Updates", url="https://t.me/Star_Moviess_Tamil"),InlineKeyboardButton("👥 Support Group",url = "https://t.me/Star_Bots_Tamil_Support") ]           ]        ) )

@Client.on_message(filters.private & filters.command(['about']))
async def about(client, message):
          await message.reply_text(text =f"<b>🤖 My Name :- <a href=https://t.me/Google_Translator_Star_Bot><b>Google Translator Star Bots</b></a>\n\n🧑🏻‍💻 Developer :- <a href=https://t.me/TG_Karthik><b>Karthik</b></a>\n\n📝 Language :- Python3\n\n📚 Framework :- Pyrogram\n\n📡 Hosted on :- VPS\n\n🤖 Bot Channel :- <a href=https://t.me/Star_Bots_Tamil><b>Star Bots Tamil</b></a>\n\n🎥 Movie Updates :- <a href=https://t.me/Star_Moviess_Tamil><b>Star Movies Tamil</b></a></b>",reply_to_message_id = message.id, disable_web_page_preview=True, parse_mode=enums.ParseMode.HTML, reply_markup=InlineKeyboardMarkup(            [                [                    InlineKeyboardButton("🤖 Bot Channel" ,url="https://t.me/Star_Bots_Tamil") ],                 [InlineKeyboardButton("🎥 Movie Updates", url="https://t.me/Star_Moviess_Tamil"),InlineKeyboardButton("👥 Support Group",url = "https://t.me/Star_Bots_Tamil_Support") ]           ]        ) )

@Client.on_message(filters.channel & filters.text)
async def qbleech(bot, message):
    original_text = message.text or ""
    if "https://" in original_text or "http://" in original_text:
        try:
            new_text = f"/qbleech {original_text}"
            await message.edit_text(new_text)
        except Exception as e:
            print(f"An error occurred: {e}")
