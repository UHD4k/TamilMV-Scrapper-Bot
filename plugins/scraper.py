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
        
<b>{no}.</b> <code>{filename}</code>
<b>┖ Links : <a href="https://t.me/share/url?url={m}">Magnet 🧲</a>  | <a href="{t['href']}">Torrent 🌐</a></b>"""
    return parse_data

async def tamilmv1(url):
    cget = create_scraper().request
    resp = cget("GET", url)
    soup = BeautifulSoup(resp.text, "html.parser")
    tor = soup.select('a[data-fileext="torrent"]')

    torrent_links = []  # List to store torrent links only
    
    for t in tor:
        torrent_link = t['href']
        filename = sub(r"www\S+|\- |\.torrent", "", t.string)
        torrent_links.append(torrent_link)
    return torrent_links
