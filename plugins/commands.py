import os
from pyrogram import Client, filters, enums
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup
)
from pyrogram.types import InlineQuery
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from plugins.core.db import u_db

OWNER_ID = int(os.environ.get("OWNER_ID", 1391556668))

@Client.on_message(filters.private & filters.command(['start']))
async def start(query: InlineQuery, message):
          await message.reply_text(text =f"<b>Hello 👋🏻 {message.from_user.first_name} ❤️\n\nI'm Star Bots Official 1TamilMV Scrapper Bot. I Can Bypass any Movie to You Sent 1TamilMV Link. You Can Sent Torrent Links and Magnet Links Seperately to Your Channel/Group.\n\nTo know How to Use me check /help.\n\nI'll Work in Inline Anywhere.</b>",reply_to_message_id = message.id, disable_web_page_preview=True, parse_mode=enums.ParseMode.HTML, reply_markup=InlineKeyboardMarkup(            [                [                    InlineKeyboardButton("🤖 Bot Channel" ,url="https://t.me/Star_Bots_Tamil"),InlineKeyboardButton("Go Inline Here",switch_inline_query_current_chat='')],                 [InlineKeyboardButton("🎥 Movie Updates", url="https://t.me/Star_Moviess_Tamil"),InlineKeyboardButton("👥 Support Group",url = "https://t.me/Star_Bots_Tamil_Support") ]           ]        ) )
  
@Client.on_message(filters.private & filters.command(['help']))
async def help(client, message):
          await message.reply_text(text =f"<b>Hey 👋🏻 {message.from_user.first_name} Follow These Steps :-\n\n● Send /bypass to 1TamilMV website Movies\n● /auto_leech to Send Torrent Links 🌐 to Leeching Group\n● /send_torrents to Send Torrent Links 🌐 to Channel\n● /send_magnets to Send Magnet Links 🧲 to Channel\n\nAvailable Commands\n\n● /start - Check if 😊 I'm Alive\n● /help - How to Use❓\n● /about - to Know About Me 😌\n\nMade by <a href=https://t.me/Star_Bots_Tamil><b></b>Star Bots Tamil</a></b>",reply_to_message_id = message.id , disable_web_page_preview=True, parse_mode=enums.ParseMode.HTML, reply_markup=InlineKeyboardMarkup(            [                [                    InlineKeyboardButton("🤖 Bot Channel" ,url="https://t.me/Star_Bots_Tamil") ],                 [InlineKeyboardButton("🎥 Movie Updates", url="https://t.me/Star_Moviess_Tamil"),InlineKeyboardButton("👥 Support Group",url = "https://t.me/Star_Bots_Tamil_Support") ]           ]        ) )

@Client.on_message(filters.private & filters.command(['about']))
async def about(client, message):
          await message.reply_text(text =f"<b>🤖 My Name :- <a href=https://t.me/TamilMV_Scrapper_Bot><b>1TamilMV Scrapper Bot</b></a>\n\n🧑🏻‍💻 Developer :- <a href=https://t.me/U_Karthik><b>Karthik</b></a>\n\n📝 Language :- Python3\n\n📚 Framework :- Pyrogram\n\n📡 Hosted on :- VPS\n\n🤖 Bot Channel :- <a href=https://t.me/Star_Bots_Tamil><b>Star Bots Tamil</b></a>\n\n🎥 Movie Updates :- <a href=https://t.me/Star_Moviess_Tamil><b>Star Movies Tamil</b></a></b>",reply_to_message_id = message.id, disable_web_page_preview=True, parse_mode=enums.ParseMode.HTML, reply_markup=InlineKeyboardMarkup(            [                [                    InlineKeyboardButton("🤖 Bot Channel" ,url="https://t.me/Star_Bots_Tamil") ],                 [InlineKeyboardButton("🎥 Movie Updates", url="https://t.me/Star_Moviess_Tamil"),InlineKeyboardButton("👥 Support Group",url = "https://t.me/Star_Bots_Tamil_Support") ]           ]        ) )

@Client.on_message(filters.command("links") & filters.private)
async def links(c: Client, m: Message):
    ''' Start Message of the Bot !!'''

    await m.reply_text(
        text='''
<b>🔰 Hello, I am TamilMVAutoRss and Multi-Tasking Bot! 🔰</b>

<b>Get All RSS Feed Channel Links</b>''',
        quote=True,
        parse_mode=enums.ParseMode.HTML,
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("1TamilMV", url="https://t.me/+3rd6z7uhqTxiYWM1")],
            [InlineKeyboardButton("1TamilBlasters", url="https://t.me/+cFk95Ozi_RA2MGE1")],
            [InlineKeyboardButton("2TamilRockers", url="https://t.me/+Un9tkoLZVz41NDk1")]
        ])
    )
    
# Add multiple domains
@Client.on_message(filters.command("set_domains") & filters.user(OWNER_ID))
async def add_domains(client: Client, message: Message):
    """
    Adds multiple domains and associates each with its website.
    Usage: /add_domains <url1> <url2> <url3>
    """
    args = message.text.split(maxsplit=3)
    
    if len(args) != 4:
        await message.reply(
            "<b>Usage :- </b><code>/set_domains [url1] [url2] [url3]</code>",
            parse_mode=enums.ParseMode.HTML,
            disable_web_page_preview=True
        )
        return

    # Extract URLs
    url1, url2, url3 = args[1], args[2], args[3]
    
    try:
        # Add domains to the database with appropriate names
        await u_db.add_or_update_domain("1TamilMV", url1)
        await u_db.add_or_update_domain("1TamilBlasters", url2)
        await u_db.add_or_update_domain("2TamilRockers", url3)

        # Send a confirmation message
        await message.reply(
            f"<b>Domains have been added/updated:</b>\n"
            f"<b>1TamilMV :- {url1}</b>\n"
            f"<b>1TamilBlasters :- {url2}</b>\n"
            f"<b>2TamilRockers :- {url3}</b>",
            parse_mode=enums.ParseMode.HTML,
            disable_web_page_preview=True
        )
    except Exception as e:
        # Log the error and notify the user
        await message.reply(
            f"<b>An error occurred while adding domains:</b> <code>{e}</code>",
            parse_mode=enums.ParseMode.HTML,
            disable_web_page_preview=True
        )

@Client.on_message(filters.command("get_domains") & filters.user(OWNER_ID))
async def get_domains(client: Client, message: Message):
    """
    Fetches and displays all available domains from the database.
    """
    try:
        # Fetch all domains from the database
        domains = await u_db.get_all_domains()
        
        if not domains:
            await message.reply("<b>No domains found in the database.</b>", disable_web_page_preview=True)
            return
        
        # Create a formatted response
        response = "<b>Available Website Domains :-</b>\n"
        for key, url in domains.items():
            response += f"<b>{key} :- {url}</b>\n"
        
        await message.reply(response, parse_mode=enums.ParseMode.HTML, disable_web_page_preview=True)
    except Exception as e:
        # Log the error and notify the user
        await message.reply(
            f"<b>An error occurred while fetching domains:</b> <code>{e}</code>",
            parse_mode=enums.ParseMode.HTML,
            disable_web_page_preview=True
        )
        
