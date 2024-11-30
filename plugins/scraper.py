from pyrogram import Client, filters
from pyrogram.types import Message
from requests_html import HTMLSession
from dataclasses import dataclass
from typing import List
from datetime import datetime

# Data classes
@dataclass
class Movie:
    name: str
    release_datetime: datetime
    poster_url: str
    screenshots: List[str]
    torrents: List['Torrent']

@dataclass
class Torrent:
    file_name: str
    torrent_link: str
    magnet_link: str

# Scraping function
def scrape_from_url(url: str) -> Movie:
    session = HTMLSession()
    response = session.get(url)
    page = response.html

    # Scrape data
    name = page.find("h3")[0].text
    release_datetime_str = page.find("time")[0].attrs["datetime"]
    date_format = "%Y-%m-%dT%H:%M:%SZ"
    release_datetime = datetime.strptime(release_datetime_str, date_format)

    img_tags = page.find("img.ipsImage")
    pics = [img.attrs["src"] for img in img_tags if img.attrs["src"].lower().split(".")[-1] in ("jpg", "jpeg", "png")]
    poster_url = pics[0] if pics else ""
    screenshots = pics[1:]

    magnet_links = [a.attrs["href"] for a in page.find("a.skyblue-button")]
    torrent_links = [a.attrs["href"] for a in page.find("a[data-fileext='torrent']")]
    file_names = [span.text.strip() for span in page.find('span[style="color:#0000ff;"]')]

    torrents = [Torrent(file_name, torrent_link, magnet_link) for file_name, torrent_link, magnet_link in zip(file_names, torrent_links, magnet_links)]
    return Movie(name, release_datetime, poster_url, screenshots, torrents)

# Command handler for /bypass
@Client.on_message(filters.command("bypass") & filters.private)
async def bypass_handler(client: Client, message: Message):
    try:
        # Extract the URL from the command
        command_parts = message.text.split()
        if len(command_parts) != 2:
            await message.reply("❌ *Usage:* `/bypass {link}`", parse_mode="markdown")
            return

        url = command_parts[1]

        # Notify user
        await message.reply("⏳ Fetching movie details, please wait...")

        # Scrape movie details
        movie = scrape_from_url(url)

        # Build the message content
        caption = f"🎥 *Movie Title*: {movie.name}\n" \
                  f"📅 *Release Date*: {movie.release_datetime.strftime('%Y-%m-%d %H:%M:%S')}\n\n" \
                  f"🔗 Below are the available torrents:\n\n"

        for torrent in movie.torrents:
            caption += f"📂 *File Name*: {torrent.file_name}\n" \
                       f"🧲 [Magnet Link]({torrent.magnet_link})\n" \
                       f"📥 [Torrent File]({torrent.torrent_link})\n\n"

        # Send movie poster and details
        await client.send_photo(
            chat_id=message.chat.id,
            photo=movie.poster_url or None,
            caption=caption,
            parse_mode="markdown"
        )
    except Exception as e:
        await message.reply(f"⚠️ An error occurred: {str(e)}")
