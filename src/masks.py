import logging

logger = logging.getLogger('masks')
file_handler = logging.FileHandler('log/my_logging.log')
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def get_mask_card_number(card_number: int) -> str:
    """Принимает на вход номер карты и возвращает ее маску."""
    str_card_number = str(card_number)
    if str_card_number.isdigit() and len(str_card_number) == 16:
        mask_card_number = str_card_number[:4] + " " + str_card_number[4:6] + "** **** " + str_card_number[-4:]
        logger.info(f'Принимается на вход номер карты {card_number} и маскируется')
        return mask_card_number
    else:
        logger.error("Ошибка")
        return ""


def get_mask_account(account_number: int) -> str:
    """Принимает на вход номер счета и возвращает его маску."""
    str_account_number = str(account_number)
    if str_account_number.isdigit() and len(str_account_number) == 20:
        mask_account_number = "**" + str_account_number[-4:]
        logger.info(f'Принимается на вход номер счета {account_number} и маскируется')
        return mask_account_number
    else:
        logger.error("Ошибка")
        return ""
