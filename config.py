from os import getenv

from dotenv import load_dotenv

load_dotenv()

API_ID = int(getenv("API_ID", 27353035))
API_HASH = getenv("API_HASH", "cf2a75861140ceb746c7796e07cbde9e")
BOT_TOKEN = getenv("BOT_TOKEN", None)
OWNER_ID = int(getenv("OWNER_ID", "6440277281"))
MONGO_URL = getenv("MONGO_URL", None)
SUPPORT_GRP = getenv("SUPPORT_GRP", "KANHA_TECH_SUPPORT")
UPDATE_CHNL = getenv("UPDATE_CHNL", "KANHA_TECH")
OWNER_USERNAME = getenv("OWNER_USERNAME", "DEADLY_KANHA")

# Random Start Images
IMG = [
    "https://graph.org/file/2c30aed72f9553fcedbfa.jpg",
]


# Random Stickers
STICKER = [
    "CAACAgUAAx0CYlaJawABBy4vZaieO6T-Ayg3mD-JP-f0yxJngIkAAv0JAALVS_FWQY7kbQSaI-geBA",

]

EMOJIOS = [
    "🤭",
    
]
