import json
import logging
from pathlib import Path
from typing import Any

import pandas as pd

from src.config import ROOTPATH

logger = logging.getLogger('utils')
file_handler = logging.FileHandler('../log/my_logging.log', mode='w')
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
                logger.info('the file was opened successfully')
                return operations
            except json.JSONDecodeError:
                logger.error(f'file decoding error {json.JSONDecodeError}')
                print("Ошибка декодирования файла.")
                return []
    except FileNotFoundError:
        logger.error(f'error {FileNotFoundError}')
        print("Файл не найден.")
        return []


file_path = Path(ROOTPATH, "../data/operations.json")
transactions = read_json_file(file_path)


csv_file = '../data/transactions.csv'
excel_file = '../data/transactions_excel.xlsx'


def read_csv():
    df_csv = pd.read_csv(csv_file, delimiter=";")
    df_csv["operationAmount"] = df_csv.apply(lambda row: {"amount": row["amount"],
                                                          "currensy": {"name": row["currency_name"],
                                                                       "code": row["currency_code"]}}, axis=1)

    new_col_order = ["id", "state", "date", "operationAmount", "description", "from", "to"]
    df_csv = df_csv[new_col_order]
    list_dict = df_csv.to_dict(orient="records")
    return list_dict


# print(read_csv())


def read_excel():
    df_excel = pd.read_excel(excel_file)
    df_excel["operationAmount"] = df_excel.apply(lambda row: {"amount": row["amount"],
                                                              "currensy": {"name": row["currency_name"],
                                                                           "code": row["currency_code"]}}, axis=1)

    new_col_order = ["id", "state", "date", "operationAmount", "description", "from", "to"]
    df_excel = df_excel[new_col_order]
    list_dict = df_excel.to_dict(orient="records")
    return list_dict


print(read_excel())
