import os
import logging

# Logging >>>
logging.getLogger("pyrogram").setLevel(logging.ERROR)
LOGGER = logging.getLogger(__name__)

class Config:
    API_ID = int(os.environ.get("API_ID", "11329245"))
    API_HASH = os.environ.get("API_HASH", "90988dcdd5ddd4d0a28843a1e2605924")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7713324413:AAGYzSbK5Z9KbhaJGiQdA7Rs-YaYLk4fNiU")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BVtsOKEBu5Pf_Oesjuxt4TIzNijt1iMjJ8hEa3xtURQFrsd0GFYLhS_XFm2iJ61NfFeKR5icfMSu_SWH3eRvvdZ-X7IyOVFZuQ4sHKoiju_WXCH4uQqqd7vB7_9hGyMbDk7mUgjVKNkRg0trupt-5mu8pAeWAZ3US61kBnLKvsMYSjiaiL3uWI3UDfzyNQzFhf_hXWF_XskD0QrMPS87wEd85iNzXBgBE9Sae2haJ8YppGWxhcGtmJDSqHnDSlxh2dFLBZ1K_o7zxE6i1FrOaqEL_gKW87xqc2W43kCsUj-s9A9GyXdP7aUxu1Mku5j3GyMxEWS79Yku7AfxyeGUYhTw5dXGScE=")
    OWNER_ID = int(os.environ.get("OWNER_ID", 1391556668))
    GROUP_ID = int(os.environ.get("GROUP_ID", -1001542301808))
    DB_URL = os.environ.get("DB_URL", "mongodb+srv://KarthikMovies:KarthikUK007@cluster0.4l5byki.mongodb.net/?retryWrites=true&w=majority")
    DB_NAME = os.environ.get("DB_NAME", "Cluster0")
    # RSS Feed URL
    TAMILMV = os.environ.get("TMV", "https://www.1tamilmv.ru/")
    TAMILBLAST = os.environ.get("TB", "https://www.1tamilblasters.my/")
    TAMILROCKERS = os.environ.get("TR", "https://www.2tamilrockers.com/")
    # log channel list
    TAMILMV_LOG = int(os.environ.get("TMV_LOG", -1001864825324))
    TAMILBLAST_LOG = int(os.environ.get("TB_LOG", -1001822541447))
    TAMILROCKERS_LOG = int(os.environ.get("TR_LOG", -1002056074553))
