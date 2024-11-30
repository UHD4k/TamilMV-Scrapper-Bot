from re import match
from urllib.parse import urlparse
from plugins.core.exceptions import DDLException
from plugins.scraper import *

fmed_list = [
    "fembed.net",
    "fembed.com",
    "femax20.com",
    "fcdn.stream",
    "feurl.com",
    "layarkacaxxi.icu",
    "naniplay.nanime.in",
    "naniplay.nanime.biz",
    "naniplay.com",
    "mm9842.com",
]


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

async def direct_link_checker1(link, client, group_id, onlylink=False):
    domain = urlparse(link).hostname

    # Scraper
    if bool(match(r"https?:\/\/.+\.1tamilmv\.\S+", link)):
        torrent_links = await tamilmv1(link)  # Call the tamilmv1 function to get torrent links
    else:
        # Handle unsupported domains or exceptions
        if bool(match(r"https?:\/\/.+\.technicalatg\.\S+", link)):
            raise DDLException("Bypass Not Allowed!")
        else:
            raise DDLException(
                f"<i>No Bypass Function Found for your Link:</i> <code>{link}</code>"
            )

    if onlylink:
        return torrent_links

    # Send each torrent link as a separate message to the group
    for torrent_link in torrent_links:
        try:
            await client.send_message(group_id, f"/qbleech {torrent_link}")
        except Exception as e:
            print(f"Error sending message for {torrent_link}: {e}")

    return torrent_links
    
