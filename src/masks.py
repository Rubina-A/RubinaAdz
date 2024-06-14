def get_mask_card_number(card_number: list[int]) -> str:
    """Принимает на вход номер карты и возвращает ее маску."""
    str_card_number = str(card_number)
    mask_card_number = str_card_number[:4] + " " + str_card_number[4:6] + "** **** " + str_card_number[-4:]

    return mask_card_number


def get_mask_account(account_number: list[int]) -> str:
    """Принимает на вход номер счета и возвращает его маску."""
    str_account_number = str(account_number)
    mask_account_number = "**" + str_account_number[-4:]

    return mask_account_number
