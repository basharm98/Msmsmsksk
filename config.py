from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID"))

PING_IMG = getenv("PING_IMG", "https://telegra.ph/file/7cf0196f135b978d6fbd3.jpg")
START_IMG = getenv("START_IMG", "https://telegra.ph/file/7cf0196f135b978d6fbd3.jpg")

SESSION = getenv("SESSION", None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/JJJJZO")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/JJJJZO")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6878497585").split()))


FAILED = "https://telegra.ph/file/7cf0196f135b978d6fbd3.jpg"
