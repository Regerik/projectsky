import pytest
from src.generators import filter_by_currency, transaction_descriptions, card_number_generator


@pytest.fixture
def transactions():
    """Фикстура с тестовыми транзакциями"""
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {"name": "USD", "code": "USD"}
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {"name": "USD", "code": "USD"}
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {
                "amount": "43318.34",
                "currency": {"name": "RUB", "code": "RUB"}
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160"
        }
    ]


def test_filter_by_currency(transactions):
    """Тест фильтрации по валюте"""
    generator = filter_by_currency(transactions, "USD")

    first = next(generator)
    assert first["id"] == 939719570
    assert first["operationAmount"]["currency"]["code"] == "USD"

    second = next(generator)
    assert second["id"] == 142264268
    assert second["operationAmount"]["currency"]["code"] == "USD"


def test_filter_by_currency_no_match(transactions):
    """Тест фильтрации по валюте, которой нет"""
    generator = filter_by_currency(transactions, "EUR")

    with pytest.raises(StopIteration):
        next(generator)


def test_filter_by_currency_empty_list():
    """Тест фильтрации с пустым списком"""
    generator = filter_by_currency([], "USD")

    with pytest.raises(StopIteration):
        next(generator)


def test_transaction_descriptions(transactions):
    """Тест получения описаний транзакций"""
    generator = transaction_descriptions(transactions)

    assert next(generator) == "Перевод организации"
    assert next(generator) == "Перевод со счета на счет"
    assert next(generator) == "Перевод со счета на счет"


def test_transaction_descriptions_empty():
    """Тест описаний с пустым списком"""
    generator = transaction_descriptions([])

    with pytest.raises(StopIteration):
        next(generator)


@pytest.mark.parametrize("start, end, expected", [
    (1, 3, ["0000 0000 0000 0001", "0000 0000 0000 0002", "0000 0000 0000 0003"]),
    (5, 7, ["0000 0000 0000 0005", "0000 0000 0000 0006", "0000 0000 0000 0007"]),
    (9999999999999999, 9999999999999999, ["9999 9999 9999 9999"])
])
def test_card_number_generator(start, end, expected):
    """Тест генерации номеров карт с параметризацией"""
    result = list(card_number_generator(start, end))
    assert result == expected
