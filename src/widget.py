from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(account_card: str) -> str:
    """Функция маскирует номер счета/карты с добавлением платежной системы счета/карты"""
    account_card_word = ""
    account_card_digits = ""
    for i in account_card:
        if i.isalpha():
            account_card_word += i
        elif i.isdigit():
            account_card_digits += i
    if len(account_card_digits) == 16:
        final_numbers = get_mask_card_number(int(account_card_digits))
    else:
        final_numbers = get_mask_account(int(account_card_digits))

    return str(account_card_word + " " + final_numbers)


def get_data(date: str) -> str:
    """Функция преобразует формат даты в день/месяц/год"""
    no_format_date = datetime.strptime(date[:10], ("%Y-%m-%d"))
    format_date = no_format_date.strftime("%d.%m.%Y")

    return format_date

