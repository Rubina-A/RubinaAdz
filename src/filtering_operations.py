import re


def description_transactions(file_transactions: list[dict], description) -> list[dict]:
    """Функция, которая принимает список словарей с данными о
    банковских операциях и строку поиска, а возвращать список
    словарей, у которых в описании есть данная строка."""
    results = []
    pattern = re.compile(description, re.IGNORECASE)

    for transaction in file_transactions:
        for key, value in transaction.items():
            if isinstance(value, str) and re.search(pattern, value):
                results.append(transaction)
                break

    return results


def count_operations_by_category(file_transactions, categories):
    """Функция, которая принимает список словарей и категории и возвращает словарь категорий, с указанием категориии
    и кол-ва соответсвубщий упоминаний ее в списке словарей"""
    category_count = {category: 0 for category in categories}

    for transaction in file_transactions:
        description = transaction.get("description", "")
        for category in categories:
            if category.lower() in description.lower():
                category_count[category] += 1

    return category_count
