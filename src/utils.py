import json
from pathlib import Path
from typing import Any

from src.config import ROOTPATH
import logging

logger = logging.getLogger('utils')
file_handler = logging.FileHandler('log/my_logging.log', mode='w')
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def read_json_file(file_path: Any) -> list[dict]:
    """Функция принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях.
    Если файл пустой, содержит не список или не найден, функция возвращает пустой список."""

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            try:
                operations = json.load(file)
                return operations
            except json.JSONDecodeError:
                logger.error(f'Ошибка дедирования файла {json.JSONDecodeError}')
                print("Ошибка декодирования файла.")
                return []
    except FileNotFoundError:
        logger.error(f'Ошибка {FileNotFoundError}')
        print("Файл не найден.")
        return []


file_path = Path(ROOTPATH, "../data/operations.json")
transactions = read_json_file(file_path)
