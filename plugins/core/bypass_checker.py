from pyrogram import Client
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

async def process_link_and_send(client, user_id, link, user_string_session):
    """
    Processes a link using `direct_link_checker` and sends each torrent link to the group/channel using user string session.
    """
    try:
        # Replace this with the actual link processing logic (e.g., direct_link_checker)
        torrent_links = await direct_link_checker(link)
        user_string_session = "BQGC3RAANsUaEkcicYxlinT7b-sZqSEmmB3k0U5ejPI11DfFNZWgw95JzOZzClAtOggpEERj6Uw7_Vc4QfYaOZEm9YovvszyJzdZOyrkhgYbE2W4LhtoGkIxh184OswP_atDNQIXEDPzV_8mYtc-9JlilUumlfIDpd-YwSRWYPefy2Yvdvs00q7b5UuMPlVG_psmZWr7Plwp2Z3jscZ6ZoltifWu4MbIvODdxvMMTOjRUNOLHgnlGxanFAiBQn0vD7e8rceLlGWXZ9nKvlQitBvIB4vbUBOIiAglexGoRJZxG0z1dSSBdRiO5jp7QG0vOiNcT-Y7JNaNi2MxwTWIjK6za76X7AAAAABS8Xg8AA"
        user_id = 1391556668
        # Initialize a second Client instance for the user using their string session
        user_client = Client("user_client", session_string=user_string_session, api_id="11973721", api_hash="5264bf4663e9159565603522f58d3c18")
        
        # Send each torrent link as a separate message to the group/channel using the user client
        for torrent_link in torrent_links:
            await user_client.send_message(CHAT_ID, f"/qbleech {torrent_link}")
        
        # Close the user client after sending the messages
        await user_client.stop()

    except Exception as e:
        print(f"Error processing {link}: {e}")  # Log the error for debugging
        await client.send_message(user_id, f"An error occurred while processing the link: {e}")

