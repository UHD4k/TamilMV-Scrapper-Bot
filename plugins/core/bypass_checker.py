from pyrogram import enums, Client
from re import match
from urllib.parse import urlparse
from plugins.core.exceptions import DDLException
from plugins.scraper import *
import os
from telethon import TelegramClient
from telethon.sessions import StringSession
import re
import time
import asyncio
import requests
from bs4 import BeautifulSoup
from plugins.Database.db import u_db
from config import Config

API_ID = int(os.environ.get("API_ID",11973721))
API_HASH = os.environ.get("API_HASH", "5264bf4663e9159565603522f58d3c18")
STRING_SESSION = os.environ.get("STRING_SESSION", "1BVtsOKEBu5Pf_Oesjuxt4TIzNijt1iMjJ8hEa3xtURQFrsd0GFYLhS_XFm2iJ61NfFeKR5icfMSu_SWH3eRvvdZ-X7IyOVFZuQ4sHKoiju_WXCH4uQqqd7vB7_9hGyMbDk7mUgjVKNkRg0trupt-5mu8pAeWAZ3US61kBnLKvsMYSjiaiL3uWI3UDfzyNQzFhf_hXWF_XskD0QrMPS87wEd85iNzXBgBE9Sae2haJ8YppGWxhcGtmJDSqHnDSlxh2dFLBZ1K_o7zxE6i1FrOaqEL_gKW87xqc2W43kCsUj-s9A9GyXdP7aUxu1Mku5j3GyMxEWS79Yku7AfxyeGUYhTw5dXGScE=")
CHAT_ID_TORRENT = int(os.environ.get("CHAT_ID_TORRENT", -1002102777380))
CHAT_ID_MAGNET = int(os.environ.get("CHAT_ID_MAGNET", -1001937895669))
GROUP_ID = int(os.environ.get("GROUP_ID", -1001542301808))

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




# TamilMV RSS Feed Scraper Function
async def tamilmv_rss(bot: Client):
    tamilmv_url = await u_db.get_domain("1TamilMV")
    if not tamilmv_url:
        print("Error: TamilMV domain not found in the database.")
        return
    main_link = []

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'Connection': 'Keep-alive',
        'sec-ch-ua-platform': '"Windows"',
    }

    global movie_dict
    movie_dict = {}
    global real_dict
    real_dict = {}
    web = requests.request("GET", tamilmv_url, headers=headers)
    soup = BeautifulSoup(web.text, 'lxml')
    linker = []
    bad_titles = []
    real_titles = []
    global movie_list
    movie_list = []

    num = 0

    temps = soup.find_all('div', {'class': 'ipsType_break ipsContained'})

    for i in range(21):
        title = temps[i].findAll('a')[0].text
        bad_titles.append(title)
        links = temps[i].find('a')['href']
        content = str(links)
        linker.append(content)

    for element in bad_titles:
        real_titles.append(element.strip())
        movie_dict[element.strip()] = None

    movie_list = list(movie_dict)

    for url in linker:
        html = requests.request("GET", url, headers=headers)
        soup = BeautifulSoup(html.text, 'lxml')
        pattern = re.compile(r"magnet:\?xt=urn:[a-z0-9]+:[a-zA-Z0-9]{40}")
        big_title = soup.find_all('a')
        all_titles = []
        file_link = []
        mag = []
        for i in soup.find_all('a', href=True):
            if i['href'].startswith('magnet'):
                mag.append(i['href'])

        for a in soup.findAll('a', {"data-fileext": "torrent", 'href': True}):
            file_link.append(a['href'])

        for title in big_title:
            if title.find('span') == None:
                pass
            else:
                if title.find('span').text.endswith('torrent'):
                    all_titles.append(title.find('span').text[19:-8])

        for p in range(0, len(mag)):
            try:
                real_dict.setdefault(movie_list[num], [])
                real_dict[movie_list[num]].append((f"/ql {file_link[p]} \n\n **{all_titles[p]}**"))
                if not await u_db.is_tamilmv_exist(all_titles[p], file_link[p], mag[p]):
                    await bot.send_message(chat_id=Config.TAMILMV_LOG,
                        text=f"<b>/qbleech {file_link[p]}\n\nFile Name :- {all_titles[p]}</b>\n\n<b>📥 Updated By <a href='https://t.me/DP_BOTZ'>1TamilMV</a></b>", disable_web_page_preview=True)
                    await app.send_message(chat_id=Config.GROUP_ID,
                        text=f"<b>/qbleech {file_link[p]}\n\nFile Name :- {all_titles[p]}</b>", disable_web_page_preview=True)
                    print(f"added working...")
                    await u_db.add_tamilmv(all_titles[p], file_link[p], mag[p])
                    await asyncio.sleep(3)
            except Exception as e:
                print(e)
                pass

        num = num + 1
    return real_dict

# tamilblasters rss feed function

async def tamilblasters(bot: Client):
    tamilblasters_url = await u_db.get_domain("1TamilBlasters")
    if not tamilblasters_url:
        print("Error: TamilBlasters domain not found in the database.")
        return
    main_link = []

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'Connection': 'Keep-alive',
        'sec-ch-ua-platform': '"Windows"',
    }

    global movie_dict
    movie_dict = {}
    global real_dict
    real_dict = {}
    web = requests.request("GET", tamilblasters_url, headers=headers)
    soup = BeautifulSoup(web.text, 'lxml')
    linker = []
    bad_titles = []
    real_titles = []
    global movie_list
    movie_list = []

    num = 0

    temps = soup.find_all('div', {'class': 'ipsType_break ipsContained'})

    for i in range(41):
        title = temps[i].findAll('a')[0].text
        bad_titles.append(title)
        links = temps[i].find('a')['href']
        content = str(links)
        linker.append(content)

    for element in bad_titles:
        real_titles.append(element.strip())
        movie_dict[element.strip()] = None

    movie_list = list(movie_dict)

    for url in linker:
        html = requests.request("GET", url, headers=headers)
        soup = BeautifulSoup(html.text, 'lxml')
        pattern = re.compile(r"magnet:\?xt=urn:[a-z0-9]+:[a-zA-Z0-9]{40}")
        big_title = soup.find_all('a')
        all_titles = []
        file_link = []
        mag = []
        for i in soup.find_all('a', href=True):
            if i['href'].startswith('magnet'):
                mag.append(i['href'])

        for a in soup.findAll('a', {"data-fileext": "torrent", 'href': True}):
            file_link.append(a['href'])
            all_titles.append(re.sub(r'www\.[a-z0-9.\-]+', '', a.text, flags=re.IGNORECASE).replace('.torrent', '').replace('-', '', 1).replace(' ', '', 2))

        for p in range(0, len(mag)):
            try:
                real_dict.setdefault(movie_list[num], [])
                real_dict[movie_list[num]].append((f"/ql {file_link[p]} \n\n **{all_titles[p]}**"))
                if not await u_db.is_tb_exist(all_titles[p], file_link[p], mag[p]):
                    await bot.send_message(chat_id=Config.TAMILBLAST_LOG,
                        text=f"<b>/qbleech {file_link[p]}\n\nFile Name :- {all_titles[p]}</b>\n\n<b>📥 Updated By <a href='https://t.me/DP_BOTZ'>1TamilBlasters</a></b>", disable_web_page_preview=True)
                    await app.send_message(chat_id=Config.GROUP_ID,
                        text=f"<b>/qbleech {file_link[p]}\n\nFile Name :- {all_titles[p]}</b>", disable_web_page_preview=True)
                    print(f"added working...")
                    await u_db.add_tb(all_titles[p], file_link[p], mag[p])
                    await asyncio.sleep(3)
            except Exception as e:
                print(e)
                pass

        num = num + 1
    return real_dict


# TamilRockers RSS Feed Scraper Function

async def tamilrockers(bot: Client):
    tamilrockers_url = await u_db.get_domain("2TamilRockers")
    if not tamilrockers_url:
        print("Error: TamilRockers domain not found in the database.")
        return
    main_link = []

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'Connection': 'Keep-alive',
        'sec-ch-ua-platform': '"Windows"',
    }

    global movie_dict
    movie_dict = {}
    global real_dict
    real_dict = {}
    web = requests.request("GET", tamilrockers_url, headers=headers)
    soup = BeautifulSoup(web.text, 'lxml')
    linker = []
    bad_titles = []
    real_titles = []
    global movie_list
    movie_list = []

    num = 0

    temps = soup.find_all('div', {'class': 'ipsType_break ipsContained'})

    for i in range(41):
        title = temps[i].findAll('a')[0].text
        bad_titles.append(title)
        links = temps[i].find('a')['href']
        content = str(links)
        linker.append(content)

    for element in bad_titles:
        real_titles.append(element.strip())
        movie_dict[element.strip()] = None

    movie_list = list(movie_dict)

    for url in linker:
        html = requests.request("GET", url, headers=headers)
        soup = BeautifulSoup(html.text, 'lxml')
        pattern = re.compile(r"magnet:\?xt=urn:[a-z0-9]+:[a-zA-Z0-9]{40}")
        big_title = soup.find_all('a')
        all_titles = []
        file_link = []
        mag = []
        for i in soup.find_all('a', href=True):
            if i['href'].startswith('magnet'):
                mag.append(i['href'])

        for a in soup.findAll('a', {"data-fileext": "torrent", 'href': True}):
            file_link.append(a['href'])
            all_titles.append(re.sub(r'www\.[a-z0-9.\-]+', '', a.text, flags=re.IGNORECASE).replace('.torrent', '').replace('-', '', 1).replace(' ', '', 2))

        for p in range(0, len(mag)):
            try:
                real_dict.setdefault(movie_list[num], [])
                real_dict[movie_list[num]].append((f"/ql {file_link[p]} \n\n **{all_titles[p]}**"))
                if not await u_db.is_tr_exist(all_titles[p], file_link[p], mag[p]):
                    await bot.send_message(chat_id=Config.TAMILROCKERS_LOG,
                        text=f"<b>/qbleech {file_link[p]}\n\nFile Name :- {all_titles[p]}</b>\n\n<b>📥 Updated By <a href='https://t.me/DP_BOTZ'>2TamilRockers</a></b>", disable_web_page_preview=True)
                    await app.send_message(chat_id=Config.GROUP_ID,
                        text=f"<b>/qbleech {file_link[p]}\n\nFile Name :- {all_titles[p]}</b>", disable_web_page_preview=True)
                    print(f"added working...")
                    await u_db.add_tr(all_titles[p], file_link[p], mag[p])
                    await asyncio.sleep(3)
            except Exception as e:
                print(e)
                pass

        num = num + 1
    return real_dict
