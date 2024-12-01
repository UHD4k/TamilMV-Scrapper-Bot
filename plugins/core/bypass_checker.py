from re import match
from urllib.parse import urlparse
from plugins.core.exceptions import DDLException
from plugins.scraper import *
import os

CHAT_ID = int(os.environ.get("CHAT_ID", -1001542301808))

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
        raise DDLException("Bypass Not Allowed !")
    else:
        raise DDLException(
            f"<i>No Bypass Function Found for your Link :</i> <code>{link}</code>"
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

async def process_link_and_send(client, link):
    """
    Processes a link using `direct_link_checker1` and sends each torrent link to the group/channel.
    """
    try:
        torrent_links = await direct_link_checker1(link)
        for torrent_link in torrent_links:
            # Send each torrent link as a separate message
            await client.send_message(CHAT_ID, f"/qbleech {torrent_link}")
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
            f"<i>No Bypass Function Found for your Link:</i> <code>{link}</code>"
        )
