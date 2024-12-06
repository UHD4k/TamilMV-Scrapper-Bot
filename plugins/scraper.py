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
        filename = sub(r"^(www\.\S+\s-\s)|\.torrent$", "", t.string.strip())
        parse_data += f"""
        
<b>{no}.</b> <code>{filename}</code>
<b>┖ Links : <a href="https://t.me/share/url?url={m['href']}">Magnet 🧲</a>  | <a href="{t['href']}">Torrent 🌐</a></b>"""
    return parse_data

async def tamilmv1(url):
    cget = create_scraper().request
    try:
        resp = cget("GET", url)
        resp.raise_for_status()
    except Exception as e:
        return f"Error fetching URL: {e}"
    
    soup = BeautifulSoup(resp.text, "html.parser")
    tor = soup.select('a[data-fileext="torrent"]')

    torrent_links = []
    
    for t in tor:
        if t.string:
            torrent_link = t['href']
            filename = re.sub(r"www\S+|\.torrent", "", t.string.strip())
            # Format the response as required
            formatted_response = f"<b>/qbleech {torrent_link}\nFilename :-</b> </code>{filename}</code>"
            torrent_links.append(formatted_response)
    
    return torrent_links

async def tamilmv2(url):
    cget = create_scraper().request
    try:
        resp = cget("GET", url)
        resp.raise_for_status()
    except Exception as e:
        return f"Error fetching URL: {e}"
    
    soup = BeautifulSoup(resp.text, "html.parser")
    tor = soup.select('a[data-fileext="torrent"]')

    torrent_links = []
    
    for t in tor:
        if t.string:
            torrent_link = t['href']
            filename = sub(r"www\S+|\.torrent", "", t.string.strip())
            torrent_links.append({'link': torrent_link, 'filename': filename})
    
    return torrent_links
