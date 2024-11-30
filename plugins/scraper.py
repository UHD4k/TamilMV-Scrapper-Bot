from cloudscraper import create_scraper
from re import sub
from bs4 import BeautifulSoup

async def tamilmv(url):
    cget = create_scraper().request
    resp = cget("GET", url)
    soup = BeautifulSoup(resp.text, "html.parser")
    mag = soup.select('a[href^="magnet:?xt=urn:btih:"]')
    tor = soup.select('a[data-fileext="torrent"]')
    parse_data = f"<b><u>{soup.title.string}</u></b>"
    for no, (t, m) in enumerate(zip(tor, mag), start=1):
        filename = sub(r"www\S+|\- |\.torrent", "", t.string)
        parse_data += f"""
        
{no}. <code>{filename}</code>
┖ <b>Links :</b> <a href="https://t.me/share/url?url={m['href'].split('&')[0]}"><b>Magnet </b>🧲</a>  | <a href="{t['href']}"><b>Torrent 🌐</b></a>"""
    return parse_data

async def tamilmv1(url):
    cget = create_scraper().request
    resp = cget("GET", url)
    soup = BeautifulSoup(resp.text, "html.parser")
    mag = soup.select('a[href^="magnet:?xt=urn:btih:"]')
    tor = soup.select('a[data-fileext="torrent"]')

    # Full response data with both magnet and torrent links
    parse_data = f"<b><u>{soup.title.string}</u></b>"

    torrent_links = []  # List to store torrent links only
    
    for no, (t, m) in enumerate(zip(tor, mag), start=1):
        filename = sub(r"www\S+|\- |\.torrent", "", t.string)
        
        # Add only torrent links to the list for the channel
        torrent_links.append(t['href'])

    # Return full data and the list of torrent links
    return torrent_links
