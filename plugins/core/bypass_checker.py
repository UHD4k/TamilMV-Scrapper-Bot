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

async def direct_link_checker1(link, onlylink=False):
    domain = urlparse(link).hostname

    # Initialize an empty list for torrent links
    torrent_links = []

    # Scraper for 1TamilMV
    if bool(match(r"https?:\/\/.+\.1tamilmv\.\S+", link)):
        result = await tamilmv1(link)
        torrent_links = extract_torrent_links(result)

    # Exceptions for specific domains
    elif bool(match(r"https?:\/\/.+\.technicalatg\.\S+", link)):
        raise DDLException("Bypass Not Allowed !")
    else:
        raise DDLException(
            f"<i>No Bypass Function Found for your Link :</i> <code>{link}</code>"
        )

    # Return only the torrent links if 'onlylink' is True
    if onlylink:
        return torrent_links

    links = []
    while True:
        try:
            links.append(torrent_links)
            # Assuming `blink` is the next link in the process, you would need to define its logic.
            blink = await direct_link_checker1(blink, onlylink=True)
            if is_excep_link(links[-1]):
                links.append("\n\n" + blink)
                break
        except Exception:
            break
    return links


def extract_torrent_links(response_data):
    """Extracts torrent links from the given response data."""
    # Assuming response_data contains links to torrents, and this function extracts them
    torrent_links = []
    if isinstance(response_data, tuple):
        parse_data, torrent_links = response_data
    elif isinstance(response_data, str):
        # Handle if the response data itself contains torrent links in the text
        torrent_links = extract_from_text(response_data)
    
    return torrent_links


def extract_from_text(text_data):
    """Function to extract torrent links from plain text."""
    # Example of extracting torrent links from plain text.
    torrent_links = []
    for line in text_data.split("\n"):
        if "torrent" in line:  # Modify this as per your criteria for identifying torrent links
            torrent_links.append(line.strip())
    return torrent_links
    
