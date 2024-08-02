from collections import Counter

from src.filtering_operations import description_transactions
from src.processing import sort_by_date
from src.utils import read_csv, read_excel, transactions
from src.widget import get_data, mask_account_card


def main():
    """Функция, которая ничего не принимает на вход, но связывает работу модулей в единое целое, выдавая все операции,
    отфильтрованные пользователем"""
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    choice = ""
    file_main = []
    while choice not in ("1", "2", "3"):
        choice = input()
        if choice not in ("1", "2", "3"):
            print("Выберите доступные варианты 1, 2 или 3: ")
    if choice == "1":
        print("Для обработки выбран JSON-файл.")
        file_main = transactions
    elif choice == "2":
        print("Для обработки выбран CSV-файл.")
        file_main = read_csv('../data/transactions.csv')
    elif choice == "3":
        print("Для обработки выбран XLSX-файл.")
        file_main = read_excel('../data/transactions_excel.xlsx')
    print("Введите статус, по которому необходимо выполнить фильтрацию. "
          "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING")

    filter_file = []
    while (user_input := input().upper()) not in ('EXECUTED', 'CANCELED', 'PENDING'):
        print(f"Статус операции {user_input} недоступен.")

    for trans in file_main:
        for key, value in trans.items():
            if value == user_input:
                filter_file.append(trans)

    print("Отсортировать операции по дате? ДА/НЕТ")
    while (user_sort_date := input().upper()) not in ('ДА', 'НЕТ', ):
        print("Выберите вариант ДА или НЕТ.")
    if user_sort_date == 'ДА':
        print("Отсортировать по возрастанию или по убыванию?")
        while (choice := input().lower()) not in ("возрастанию" or "убыванию"):
            print("Введите критерий сортировки.")
            if choice == "возрастанию":
                filter_file = sort_by_date(filter_file)
            else:
                filter_file = sort_by_date(filter_file, reverse=False)

    print("Выводить только рублевые тразакции? ДА/НЕТ")
    while (user_ruble := input().upper()) not in ('ДА', 'НЕТ',):
        print("Выберите вариант ДА или НЕТ.")
    filter_file_ruble = []
    if user_ruble == 'ДА':
        for trans in filter_file:
            if trans["operationAmount"]["currency"]["code"] == "RUB":
                filter_file_ruble.append(trans)
    else:
        filter_file_ruble = filter_file

    print("Отфильтровать список транзакций по определенному слову в описании? ДА/НЕТ")
    while (user := input().upper()) not in ('ДА', 'НЕТ', ):
        print("Выберите вариант ДА или НЕТ.")

    if user == 'ДА':
        print("Введите слово для поиска в описании: ")
        user_category = input()
        file_transactions = description_transactions(filter_file_ruble, user_category)
    else:
        file_transactions = filter_file_ruble

    keys = [trans['description'] for trans in file_transactions]
    counter = Counter(keys)

    sum_trans = 0

    for k, v in counter.items():
        sum_trans += v

    if len(file_transactions) <= 0:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
    else:
        print(f"Всего банковских операций в выборке: {sum_trans}")
        for trans in file_transactions:
            print(f"{get_data(trans["date"])} {trans["description"]}")
            if "Перевод" in trans["description"]:
                print(f"{mask_account_card(trans["from"])} -> {mask_account_card(trans["to"])}")
            else:
                print(mask_account_card(trans["to"]))
            print(f"Сумма: {trans["operationAmount"]["amount"]} "
                  f"{trans["operationAmount"]["currency"]["name"]}")


main()
