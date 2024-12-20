from pyrogram import enums
from re import match
from urllib.parse import urlparse
from plugins.core.exceptions import DDLException
from plugins.scraper import *
import os, asyncio
from telethon import TelegramClient, events
from telethon.sessions import StringSession

API_ID = int(os.environ.get("API_ID",11973721))
API_HASH = os.environ.get("API_HASH", "5264bf4663e9159565603522f58d3c18")
STRING_SESSION = os.environ.get("STRING_SESSION", "1BVtsOKEBu5Pf_Oesjuxt4TIzNijt1iMjJ8hEa3xtURQFrsd0GFYLhS_XFm2iJ61NfFeKR5icfMSu_SWH3eRvvdZ-X7IyOVFZuQ4sHKoiju_WXCH4uQqqd7vB7_9hGyMbDk7mUgjVKNkRg0trupt-5mu8pAeWAZ3US61kBnLKvsMYSjiaiL3uWI3UDfzyNQzFhf_hXWF_XskD0QrMPS87wEd85iNzXBgBE9Sae2haJ8YppGWxhcGtmJDSqHnDSlxh2dFLBZ1K_o7zxE6i1FrOaqEL_gKW87xqc2W43kCsUj-s9A9GyXdP7aUxu1Mku5j3GyMxEWS79Yku7AfxyeGUYhTw5dXGScE=")
CHAT_ID_TORRENT = int(os.environ.get("CHAT_ID_TORRENT", -1002102777380))
CHAT_ID_MAGNET = int(os.environ.get("CHAT_ID_MAGNET", -1001937895669))
GROUP_ID = int(os.environ.get("GROUP_ID", -1001542301808))
#SOURCE_CHANNELS = list(
#    map(int, os.environ.get("SOURCE_CHANNELS", "-1001822541447 -1002056074553 -1001864825324").split(" "))
#)
SOURCE_CHANNEL = int(os.environ.get("SOURCE_CHANNEL", -1001864825324))
SOURCE_CHANNEL_1 = int(os.environ.get("SOURCE_CHANNEL_1", -1001822541447))
SOURCE_CHANNEL_2 = int(os.environ.get("SOURCE_CHANNEL_2", -100182254848494847))
DESTINATION_CHANNEL = int(os.environ.get("DESTINATION_CHANNEL", -1001542301808))
DESTINATION_CHANNEL_1 = int(os.environ.get("DESTINATION_CHANNEL_1", -1001542301808))
DESTINATION_CHANNEL_2 = int(os.environ.get("DESTINATION_CHANNEL_2", -1001542301808))

app = TelegramClient(StringSession(STRING_SESSION), API_ID, API_HASH).start()

# Main Bypass
def is_excep_link(url):
    return bool(
        match(
            r"https?:\/\/.+\.(1tamilmv|gdtot|filepress|pressbee|gdflix|sharespark)\.\S+|https?:\/\/(sharer|onlystream|hubdrive|katdrive|drivefire|skymovieshd|toonworld4all|kayoanime|cinevood|gdflix|filepress|pressbee|filebee|appdrive)\.\S+",
            url,
        )
    )

async def direct_link_checker(link, onlylink=False):
    domain = urlparse(link).hostname

    # Scraper 
    if bool(match(r"https?:\/\/.+\.1tamilmv\.\S+", link)):
        return await tamilmv(link)
    elif bool(match(r"https?:\/\/.+\.1tamilmv\.\S+", link)):
        return await tamilmv1(link)
    elif bool(match(r"https?:\/\/.+\.1tamilmv\.\S+", link)):
        return await tamilmv2(link)
        
    # Exceptions
    elif bool(match(r"https?:\/\/.+\.technicalatg\.\S+", link)):
        raise DDLException("<b>Bypass Not Allowed !</b>")
    else:
        raise DDLException(
            f"<b>No Bypass Function Found for your Link :</b> <code>{link}</code>"
        )

    if onlylink:
        return blink

    links = []
    while True:
        try:
            links.append(blink)
            blink = await direct_link_checker(blink, onlylink=True)
            if is_excep_link(links[-1]):
                links.append("\n\n" + blink)
                break
  
        except Exception:
            break
    return links

# Send Torrents Links
async def process_link_and_send(client, link):
    """
    Processes a link using `direct_link_checker1` and sends each torrent link to the group/channel.
    """
    try:
        torrent_links = await direct_link_checker1(link)
        for torrent_link in torrent_links:
            # Send each torrent link as a separate message
            await client.send_message(CHAT_ID_TORRENT, f"{torrent_link}")
    except Exception as e:
        print(f"Error processing {link}: {e}")  # Log the error for debugging

async def direct_link_checker1(link):
    """
    Processes a link and extracts torrent links using `tamilmv1`.
    """
    if bool(match(r"https?:\/\/.+\.1tamilmv\.\S+", link)):
        return await tamilmv1(link)
    else:
        raise DDLException(
            f"<b>No Bypass Function Found for your Link:</b> <code>{link}</code>"
        )

# Send Magnet Links
async def process_link_and_send1(client, link):
    """
    Processes a link using `direct_link_checker2` and sends each torrent link to the group/channel.
    """
    try:
        magnet_links = await direct_link_checker2(link)
        for magnet_link in magnet_links:
            # Send each torrent link as a separate message
            await client.send_message(CHAT_ID_MAGNET, f"{magnet_link}")
    except Exception as e:
        print(f"Error processing {link}: {e}")  # Log the error for debugging
           
async def direct_link_checker2(link):
    """
    Processes a link and extracts magnet links using `tamilmv1`.
    """
    if bool(match(r"https?:\/\/.+\.1tamilmv\.\S+", link)):
        return await tamilmv2(link)
    else:
        raise DDLException(
            f"<b>No Bypass Function Found for your Link:</b> <code>{link}</code>"
        )

# Send Torrents Links in Group
async def process_link_and_sendg(client, link):
    """
    Processes a link using `direct_link_checker1` and sends each torrent link to the group/channel.
    """
    try:
        torrent_links = await direct_link_checker1(link)
        for torrent_link in torrent_links:
            # Send each torrent link as a separate message
            await app.send_message(GROUP_ID, f"{torrent_link}")
    except Exception as e:
        print(f"Error processing {link}: {e}")  # Log the error for debugging

@app.on(events.NewMessage(chats=SOURCE_CHANNEL))  # Listen to multiple source channels
async def forward_message(event):
    try:
        await asyncio.sleep(300)
        if event.message.media:  # If the message has media
            await event.client.send_message(DESTINATION_CHANNEL, event.message)
        else:  # If the message is text-only
            await event.client.send_message(DESTINATION_CHANNEL, event.message.text)
    except Exception as e:
        print(f"Failed to forward the message: {str(e)}")
        
@app.on(events.NewMessage(chats=SOURCE_CHANNEL_1))  # Listen to multiple source channels
async def forward_message(event):
    try:
        await asyncio.sleep(300)
        if event.message.media:
            await event.client.send_message(DESTINATION_CHANNEL_1, event.message)
        else:  # If the message is text-only
            modified_text = event.message.text.replace("/qbleech", "/qbleech1")
            await event.client.send_message(DESTINATION_CHANNEL_1, modified_text)
    except Exception as e:
        print(f"Failed to forward the message: {str(e)}")

#@app.on(events.NewMessage(chats=SOURCE_CHANNEL_2))  # Listen to multiple source channels
#async def forward_message(event):
#    try:
#        await asyncio.sleep(300)
#        if event.message.media:
#            await event.client.send_message(DESTINATION_CHANNEL_2, event.message)
#        else:  # If the message is text-only
#            modified_text = event.message.text.replace("/qbleech", "/qbleech2")
#            await event.client.send_message(DESTINATION_CHANNEL_2, modified_text)
#    except Exception as e:
#        print(f"Failed to forward the message: {str(e)}")
