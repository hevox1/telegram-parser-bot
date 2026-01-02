import os
from dotenv import load_dotenv

# Загружаем переменные из .env
load_dotenv()

# Получаем токен бота
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Айди админа
ADMIN_ID = [7313627424]

# данные бд
DB_HOST = 'localhost'
DB_PORT = 5432
DB_NAME = 'bot_db'
DB_USER = 'postgres'
DB_PASS = 'password'