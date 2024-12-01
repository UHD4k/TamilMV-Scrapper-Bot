from bot import user_client  # Import user_client
from pyrogram import Client
from re import match
from urllib.parse import urlparse
from plugins.core.exceptions import DDLException
from plugins.scraper import *
import os

CHAT_ID = int(os.environ.get("CHAT_ID", -1001542301808))  # Replace with your actual chat ID

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

    # Exceptions
    elif bool(match(r"https?:\/\/.+\.technicalatg\.\S+", link)):
        raise DDLException("Bypass Not Allowed!")
    else:
        raise DDLException(
            f"<i>No Bypass Function Found for your Link:</i> <code>{link}</code>"
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

async def direct_link_checker1(link, onlylink=False):
    # Scraper logic
    domain = urlparse(link).hostname
    if bool(match(r"https?:\/\/.+\.1tamilmv\.\S+", link)):
        return await tamilmv(link)
    elif bool(match(r"https?:\/\/.+\.1tamilmv\.\S+", link)):
        return await tamilmv1(link)
    elif bool(match(r"https?:\/\/.+\.technicalatg\.\S+", link)):
        raise DDLException("Bypass Not Allowed !")
    else:
        raise DDLException(
            f"<i>No Bypass Function Found for your Link :</i> <code>{link}</code>"
        )

async def process_link_and_send(client, user_id, link):
    try:
        # Process link and extract torrent links
        torrent_links = await direct_link_checker1(link)
        user_id = 1391556668
        # Send each torrent link to the group/channel using user_client
        await user_client.start()  # Start user_client
        for torrent_link in torrent_links:
            await user_client.send_message(CHAT_ID, f"/qbleech {torrent_link}")
        await user_client.stop()  # Stop user_client

        # Send confirmation to the user
        await client.send_message(user_id, "Torrent links have been successfully sent to the group/channel!")
    except Exception as e:
        print(f"Error processing {link}: {e}")
        await client.send_message(user_id, f"An error occurred: {e}")
