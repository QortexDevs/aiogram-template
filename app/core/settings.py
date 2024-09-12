import os
from pathlib import Path

from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent.parent
dotenv_path = os.path.join(BASE_DIR, ".env")


if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

env = os.environ

TELEGRAM_BOT_TOKEN = env.get("TELEGRAM_BOT_TOKEN")

REDIS_HOST = env.get("REDIS_HOST")
REDIS_PORT = env.get("REDIS_PORT")
REDIS_URL = f"redis://{REDIS_HOST}:{REDIS_PORT}/0"
