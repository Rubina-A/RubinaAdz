import pytest

from src.widget import mask_account_card, get_data

@pytest.mark.parametrize("value, expected", [
    ("2002-11-11T02:26:18.671407", "11.11.2002"),
    ("2010-06-12T02:26:18.671407", "12.06.2010"),
    ("2024-01-13T02:26:18.671407", "13.01.2024"),
    ("2025-07-14T02:26:18.671407", "14.07.2025"),
])
def test_get_data(value, expected):
    assert get_data(value) == expected

def test_mask_account_card():
    assert mask_account_card("Maestro 7000 7922 8960 6361") == "Maestro 7000 79** **** 6361"
    assert mask_account_card("Счет 73654108430135874305") == "Счет **4305"
    assert mask_account_card("Maestro 7000 7922 8960 6361") == "Maestro 7000 79** **** 6361"
    assert mask_account_card("Maestro 7000 7922 8960 2555") == "Maestro 7000 79** **** 2555"
    assert mask_account_card("Maestro 2002 7922 8960 6361") == "Maestro 2002 79** **** 6361"
    assert mask_account_card("Счет 73654108430135872131") == "Счет **2131"
    assert mask_account_card("Счет 73654108430135874529") == "Счет **4529"