from os import getenv
from dotenv import load_dotenv

load_dotenv()

API_ID = int(getenv("API_ID", "27383453"))
API_HASH = getenv("API_HASH", "4c246fb0c649477cc2e79b6a178ddfaa")
BOT_TOKEN = getenv("BOT_TOKEN", "")

OWNER_ID = int(getenv("OWNER_ID", "8508338965"))
OWNER_USERNAME = getenv("OWNER_USERNAME", "KanhaaOp")
MONGO_DB_URI = getenv("MONGO_DB_URI", "")
MUST_JOIN = getenv("MUST_JOIN", "AnupriyaUpdate")
START_IMG = getenv("START_IMG", "https://i.ibb.co/DfVvdjH7/x.jpg")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "Kanhaxduniya")
UPDATE_CHANNEL = getenv("UPDATE_CHANNEL", "AnupriyaUpdate")
