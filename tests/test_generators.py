from src.generators import filter_by_currency, transaction_descriptions, card_number_generator

import pytest

def test_transaction_descriptions():
    transactions = [
        {"description": "Перевод организации"},
        {"description": "Перевод со счета на счет"},
        {"description": "Перевод со счета на счет"},
        {"description": "Перевод с карты на карту"},
        {"description": "Перевод организации"},
    ]

    descriptions = list(transaction_descriptions(transactions))
    expected = [
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод со счета на счет",
        "Перевод с карты на карту",
        "Перевод организации"
    ]

    assert descriptions == expected

def test_card_number_generator():
    generator = card_number_generator(1, 10)
    assert next(generator) == "0000 0000 0000 0001"
    assert next(generator) == "0000 0000 0000 0002"
    assert next(generator) == "0000 0000 0000 0003"
    assert next(generator) == "0000 0000 0000 0004"
    assert next(generator) == "0000 0000 0000 0005"
    assert next(generator) == "0000 0000 0000 0006"
    assert next(generator) == "0000 0000 0000 0007"
    assert next(generator) == "0000 0000 0000 0008"
    assert next(generator) == "0000 0000 0000 0009"
    assert next(generator) == "0000 0000 0000 0010"