from typing import Dict, List


def filter_by_state(inform: List, state: str = "EXECUTED") -> List:
    """Функция запускает цикл по принимает на вход список словарей и значение для ключа
     и возвращает новый список, содержащий только те словари,
     у которых ключ содержит переданное в функцию значение"""

    new_list = []

    for k in inform:
        if k["state"] == state:
            new_list.append(k)

    return new_list


def sort_by_date(date_list: List[Dict], reverse: bool = True) -> list[dict]:
    """Функция сортирует списки словарей по по убыванию даты"""
    sorted_list = sorted(date_list, key=lambda date_entry: date_entry["date"], reverse=reverse)

    return sorted_list
