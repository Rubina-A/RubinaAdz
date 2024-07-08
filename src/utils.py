import json
from pathlib import Path
from typing import Any

from src.config import ROOTPATH


def read_json_file(file_path: Any) -> list[dict]:
    """Функция принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях.
    Если файл пустой, содержит не список или не найден, функция возвращает пустой список."""

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            try:
                operations = json.load(file)
                return operations
            except json.JSONDecodeError:
                print("Ошибка декодирования файла.")
                return []
    except FileNotFoundError:
        print("Файл не найден.")
        return []


file_path = Path(ROOTPATH, "../data/operations.json")
transactions = read_json_file(file_path)
