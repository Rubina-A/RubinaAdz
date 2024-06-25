from src.generators import filter_by_currency, transaction_descriptions, card_number_generator

import pytest

def test_transaction_descriptions(new_list):
    assert transaction_descriptions(new_list) == "Перевод организации"

def test_filter_by_currency(new_list, "USD"):
    assert transaction_descriptions(new_list) == 939719570

def test_card_number_generator(0, 0):
    assert card_number_generator(0, 0) == "0000 0000 0000 0001"