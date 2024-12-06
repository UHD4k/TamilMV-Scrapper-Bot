from asyncio import create_task, gather
from pyrogram import Client, filters
from pyrogram.filters import command, user
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, InlineQueryResultArticle, InputTextMessageContent
from pyrogram.enums import MessageEntityType
from pyrogram.errors import QueryIdInvalid
import os, re
from plugins.core.bypass_checker import direct_link_checker, direct_link_checker1, is_excep_link, process_link_and_send
from plugins.core.bot_utils import convert_time, BypassFilter, BypassFilter1
from time import time
from telethon import TelegramClient
from telethon.sessions import StringSession

API_ID = int(os.environ.get("API_ID",11973721))
API_HASH = os.environ.get("API_HASH", "5264bf4663e9159565603522f58d3c18")
STRING_SESSION = os.environ.get("STRING_SESSION", "1BVtsOKEBu5Pf_Oesjuxt4TIzNijt1iMjJ8hEa3xtURQFrsd0GFYLhS_XFm2iJ61NfFeKR5icfMSu_SWH3eRvvdZ-X7IyOVFZuQ4sHKoiju_WXCH4uQqqd7vB7_9hGyMbDk7mUgjVKNkRg0trupt-5mu8pAeWAZ3US61kBnLKvsMYSjiaiL3uWI3UDfzyNQzFhf_hXWF_XskD0QrMPS87wEd85iNzXBgBE9Sae2haJ8YppGWxhcGtmJDSqHnDSlxh2dFLBZ1K_o7zxE6i1FrOaqEL_gKW87xqc2W43kCsUj-s9A9GyXdP7aUxu1Mku5j3GyMxEWS79Yku7AfxyeGUYhTw5dXGScE=")

app = TelegramClient(StringSession(STRING_SESSION), API_ID, API_HASH).start()

# Configs
id_pattern = re.compile(r'^.\d+$') 
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMINS', '1391556668 1242556540').split()]
AUTO_BYPASS = bool(os.getenv("AUTO_BYPASS", "False") == "True")
CHAT_ID = int(os.environ.get("CHAT_ID", -1001542301808))

# Main bypass handler function
@Client.on_message(BypassFilter & (filters.user(ADMINS)))
async def bypass(client, message):
    uid = message.from_user.id
    if (reply_to := message.reply_to_message) and (
        reply_to.text or reply_to.caption
    ):
        txt = reply_to.text or reply_to.caption
        entities = reply_to.entities or reply_to.caption_entities
    elif AUTO_BYPASS or len(message.text.split()) > 1:
        txt = message.text
        entities = message.entities
    else:
        return await message.reply("<b>No Link Provided!</b>")

    wait_msg = await message.reply("<b>Bypassing...</b>")
    start = time()

    links = []
    tasks = []
    for entity in entities:
        if entity.type in (MessageEntityType.URL, MessageEntityType.TEXT_LINK):
            link = txt[entity.offset : entity.offset + entity.length]
            links.append(link)
            tasks.append(create_task(direct_link_checker(link)))

    results = await gather(*tasks, return_exceptions=True)

    output = []
    for result, link in zip(results, links):
        if isinstance(result, Exception):
            output.append(f"┖ <b>Error:</b> {result}")
        else:
            output.append(f"┖ <b>Bypass Link:</b> {result}")

    elapsed = time() - start
    reply_text = "\n".join(output)
    reply_text += f"\n\n<b>Total Links: {len(links)}</b>\n<b>Time: {convert_time(elapsed)}</b>"
    await wait_msg.edit(reply_text)

@Client.on_message(BypassFilter1 & filters.user(ADMINS))
async def send_torrents(client, message):
    if (reply_to := message.reply_to_message) and (
        reply_to.text or reply_to.caption
    ):
        txt = reply_to.text or reply_to.caption
        entities = reply_to.entities or reply_to.caption_entities
    elif AUTO_BYPASS or len(message.text.split()) > 1:
        txt = message.text
        entities = message.entities
    else:
        await message.reply("<b>No links provided!</b>")
        return

    links = []
    tasks = []

    for entity in entities:
        if entity.type in (MessageEntityType.URL, MessageEntityType.TEXT_LINK):
            link = txt[entity.offset:entity.offset + entity.length]
            links.append(link)
            tasks.append(create_task(process_link_and_send(app, link)))

    if tasks:
        results = await gather(*tasks, return_exceptions=True)
        for result in results:
            if isinstance(result, Exception):
                print(f"Error during processing: {result}")
        await message.reply("<b>Torrent Links Sent Successfully!</b>")
    else:
        await message.reply("<b>No valid links found in the message!</b>")
        
# Inline query for bypass
@Client.on_inline_query()
async def inline_query(client, query):
    text = query.query.strip()
    if text.startswith("!bp "):
        link = text[4:]
        start = time()
        try:
            result = await direct_link_checker(link, True)
            elapsed = time() - start
            response = f"┎ <b>Source Link:</b> {link}\n┖ <b>Bypass Link:</b> {result}\n\n<b>Time: {convert_time(elapsed)}</b>"
        except Exception as e:
            response = f"<b>Error:</b> {e}"

        answer = InlineQueryResultArticle(
            title="Bypass Result",
            input_message_content=InputTextMessageContent(response, disable_web_page_preview=True),
            description=f"Bypass link: {link}",
        )
        await query.answer(results=[answer], cache_time=0)
    else:
        help_text = """<b><i>1TamilMV Scrapper Bot</i></b>
        
<b>Use the inline query format: !bp [link]</b>
"""
        answer = InlineQueryResultArticle(
            title="Bypass Help",
            input_message_content=InputTextMessageContent(help_text),
        )
        await query.answer(results=[answer], cache_time=0)
