import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
VT_API_KEY = os.getenv("VT_API_KEY")
DATABASE_URL = os.getenv("DATABASE_URL")
REDIS_URL = os.getenv("REDIS_URL")

# Проверка загрузки
print("BOT_TOKEN:", BOT_TOKEN)
print("DATABASE_URL:", DATABASE_URL)