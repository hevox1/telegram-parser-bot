import logging
import colorama
from colorama import Fore, Style
from datetime import datetime

# инициализация колорамы
colorama.init(autoreset=True)

# Настройка логирования
logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

"""Словарь цветов, для разных типов сообщений"""
colors = {
    "INFO": Fore.WHITE,
    "SUCCESS": Fore.GREEN,
    "WARNING": Fore.YELLOW,
    "ERROR": Fore.RED,
    "ADMIN": Fore.MAGENTA
}

def log(user_id, action, details="", type="INFO"):
    # Получаем текущее время
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # Выбираем цвет по типу сообщения
    color = colors.get(type.upper(), Fore.WHITE)
    # Формируем строку
    log_str = f"[{time}] - {type.upper()} - {user_id}: {action}, {details}"
    # Печатаем в консоль с цветом
    print(color + log_str + Style.RESET_ALL)

