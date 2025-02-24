from os import getenv


API_ID = int(getenv("API_ID", "23680771"))
API_HASH = getenv("API_HASH", "0c58f3e3fecefc4a9d8e5bcf6968a106")
BOT_TOKEN = getenv("BOT_TOKEN", "")
OWNER_ID = list(map(int, getenv("OWNER_ID", "7091230649 6107581019").split()))
MONGO_DB = getenv("MONGO_DB", "")

CHANNEL_ID = int(getenv("CHANNEL_ID", "https://t.me/c/2444405063"))
PREMIUM_LOGS = int(getenv("PREMIUM_LOGS", ""))


