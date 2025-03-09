import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID", "22457156"))
API_HASH = getenv("API_HASH", "6787a66c5c7d4018a01fe4d5d7249992")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN", "8059284115:AAGN4Q8I-EZRKkVhgFVQNqYFfsIKnF05PIs")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://GunayMusicBot:GunayMusicBot@gunaymusicbot.uk74g.mongodb.net/?retryWrites=true&w=majority")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 99999999999))

SONG_DOWNLOAD_DURATION = int(
    getenv("SONG_DOWNLOAD_DURATION_LIMIT", "180")
)  # Remember to give value in Minutes

# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("LOGGER_ID", "-1002442606881"))

# Get this value from @MissRose_Bot on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", "7925819123"))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", None)
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY", None)

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/xSanalOwner/Gunel",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/GunayBoots/5")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/DeathTimeGroup")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", None))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from @SessionMotherBot on Telegram
STRING1 = getenv("STRING_SESSION", "AgFWq0QADFpcy71AIF4VGh3B_WD8iGLwsjpnipJYT38LKy_Kc7koYQOgJSYwUarYQ2FWAOuLvsbvxkTYhQaNWR6Eiu1I2SCLaY1NWbMrop0YKsDQ4IcgnwvTIJqw0LxR4JTxXW9QWxirsznBIjEq9a3QrU-IGmrFZocXB1c5C3LISrGQJu3ZVV1ynDRKF7UqPus2CARxIS4Keio9re15WMsTQOnszc5f6bEpUN5fR5Pinsd_-2vnslCWLckAeE0_gF9UW7_7MjIr-16oZcgHDnINv41HgcB6hIAFAOOEFWYhjxzd7rsk916j-ANN9ReVoI9icxX2h-4BMV63oDAgRsmyyO6zhAAAAAGurfq1AA")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


#  ____    _    _  ___  ___   _   __  __ _   _ ____ ___ ____   ____   ___ _____ 
# / ___|  / \  | |/ / |/ / | | | |  \/  | | | / ___|_ _/ ___| | __ ) / _ \_   _|
# \___ \ / _ \ | ' /| ' /| | | | | |\/| | | | \___ \| | |     |  _ \| | | || |  
#  ___) / ___ \| . \| . \| |_| | | |  | | |_| |___) | | |___  | |_) | |_| || |  
# |____/_/   \_\_|\_\_|\_\\___/  |_|  |_|\___/|____/___\____| |____/ \___/ |_|  
                                                                               



BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://telegra.ph/file/742235264ba8c786e5954.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://telegra.ph/file/742235264ba8c786e5954.jpg"
)
PLAYLIST_IMG_URL = "https://telegra.ph/file/742235264ba8c786e5954.jpg"
STATS_IMG_URL = "https://telegra.ph/file/742235264ba8c786e5954.jpg"
TELEGRAM_AUDIO_URL = "https://telegra.ph/file/742235264ba8c786e5954.jpg"
TELEGRAM_VIDEO_URL = "https://telegra.ph/file/742235264ba8c786e5954.jpg"
STREAM_IMG_URL = "https://telegra.ph/file/742235264ba8c786e5954.jpg"
SOUNCLOUD_IMG_URL = "https://telegra.ph/file/742235264ba8c786e5954.jpg"
YOUTUBE_IMG_URL = "https://telegra.ph/file/742235264ba8c786e5954.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://telegra.ph/file/742235264ba8c786e5954.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://telegra.ph/file/742235264ba8c786e5954.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://telegra.ph/file/742235264ba8c786e5954.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )

    
SONG_DOWNLOAD_DURATION_LIMIT = int(
    time_to_seconds(f"{SONG_DOWNLOAD_DURATION}:00")
)




