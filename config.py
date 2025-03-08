import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID", "19485442"))
API_HASH = getenv("API_HASH", "a03fcb372b3ec4e406b5d52f84b02e53")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN", "8129962630:AAFr9JBeO_5TnOzSrV3igASX1ipR7C0mc8c")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://rahidindi:rahidindi_1234@cluster0.ifslufs.mongodb.net/?retryWrites=true&w=majority")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 99999999999))

SONG_DOWNLOAD_DURATION = int(
    getenv("SONG_DOWNLOAD_DURATION_LIMIT", "180")
)  # Remember to give value in Minutes

# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("LOGGER_ID", "-1002400247577"))

# Get this value from @MissRose_Bot on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", "6931133289"))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", "yasi")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY", "HRKU-2a9c7792-2b26-4876-aebd-8a0b166769b5")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/RahidBot/EliteMusic",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv(
    "GIT_TOKEN", "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"
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/BotlarAz/152")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/sohbetgrandteam")

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
STRING1 = getenv("STRING_SESSION", "AgEpUwIAiO9u_aacpp2AAyUIHqL73Rxxld0e8tC9EmZrI_M0agUNmb8wadjc1_vWbDYkNeQC9q_3YG47I1PeC5Uc2czlp7NluW0PAk3OtY7LxLD3jcDWJyzcoHhX8VfLB3zJunSIbonUSfqpLhpUpVyTg5ulDJpuri-EEOdsNDQ84tP1nLXMBHBTUF0pONYcWzv-4utT2dOp0ibEAsmnHmfHsux8UhJeng-4ssRCiO-JJDRX5EkBf1i3UMBhoOtlQfaVQYts9fSjHbHw-N3ddE_DLsx5hMKooP5rw4b6F3QtzzdZ-yF6YG9PfRlAXsB7T4rar5jkFBkDcMCBSQrI-58US6DoywAAAAHQVlIoAA")
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
    "START_IMG_URL", "https://files.catbox.moe/8wngcz.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://files.catbox.moe/8wngcz.jpg"
)
PLAYLIST_IMG_URL = "https://files.catbox.moe/8wngcz.jpg"
STATS_IMG_URL = "https://files.catbox.moe/8wngcz.jpg"
TELEGRAM_AUDIO_URL = "https://files.catbox.moe/8wngcz.jpg"
TELEGRAM_VIDEO_URL = "https://files.catbox.moe/8wngcz.jpg"
STREAM_IMG_URL = "https://files.catbox.moe/8wngcz.jpg"
SOUNCLOUD_IMG_URL = "https://files.catbox.moe/8wngcz.jpg"
YOUTUBE_IMG_URL = "https://files.catbox.moe/8wngcz.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://files.catbox.moe/8wngcz.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://files.catbox.moe/8wngcz.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://files.catbox.moe/8wngcz.jpg"


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




