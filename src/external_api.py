from typing import Any

import requests


def transfer_to_rubles(transaction: Any) -> float:
    """Функцию, которая принимает на вход транзакцию и возвращает сумму транзакции в рублях"""

    amount = transaction["operationAmount"]["amount"]
    currency = transaction["operationAmount"]["currency"]["code"]
    url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency}&amount={amount}"
    headers = {"apikey": "5oV2nE2MypaUnRFxCR4rQ2NJJ07tY0Sa"}
    response = requests.request("GET", url, headers=headers)
    result = response.json()
    return round(result["result"], 2)
