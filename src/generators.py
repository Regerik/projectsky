"""
Модуль с функциями-генераторами для обработки транзакций
"""


def filter_by_currency(transactions, currency_code):
    """
    Генератор, который фильтрует транзакции по валюте

    Аргументы:
        transactions: список словарей с транзакциями
        currency_code: код валюты для фильтрации (например, "USD")

    Возвращает:
        Итератор с транзакциями, где валюта совпадает с заданной
    """
    for transaction in transactions:
        if transaction.get("operationAmount", {}).get("currency", {}).get("code") == currency_code:
            yield transaction


def transaction_descriptions(transactions):
    """
    Генератор, который возвращает описания транзакций

    Аргументы:
        transactions: список словарей с транзакциями

    Возвращает:
        Итератор с описаниями транзакций
    """
    for transaction in transactions:
        yield transaction.get("description", "")


def card_number_generator(start, end):
    """
    Генератор номеров банковских карт в формате XXXX XXXX XXXX XXXX

    Аргументы:
        start: начальное значение диапазона
        end: конечное значение диапазона

    Возвращает:
        Итератор с номерами карт
    """
    for number in range(start, end + 1):
        card_str = f"{number:016d}"
        formatted = f"{card_str[:4]} {card_str[4:8]} {card_str[8:12]} {card_str[12:16]}"
        yield formatted
