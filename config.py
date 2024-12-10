import os
import logging

# Logging >>>
logging.getLogger("pyrogram").setLevel(logging.ERROR)
LOGGER = logging.getLogger(__name__)

class Config:
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
