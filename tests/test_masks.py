import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize("card_number, mask_card_number", [
    (7000792289606361, "7000 79** **** 6361"),
    (7013852289602061, "7013 85** **** 2061"),
    (2005792289606361, "2005 79** **** 6361"),
    (7000792289601514, "7000 79** **** 1514"),
])
def test_get_mask_card_number(card_number, mask_card_number):
    assert get_mask_card_number(card_number) == mask_card_number


@pytest.mark.parametrize("account_number, mask_account_number", [
    (73635108430135871515, "**1515"),
    (65854108430135872585, "**2585"),
    (73654108530135874310, "**4310"),
    (73654108459135874205, "**4205"),
])
def test_get_mask_account(account_number, mask_account_number):
    assert get_mask_account(account_number) == mask_account_number
