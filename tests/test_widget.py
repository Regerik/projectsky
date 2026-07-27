"""
Тесты для модуля widget
"""

from src.widget import mask_account_card, get_date


def test_mask_account_card():
    """Тестируем маскировку карт и счетов"""
    # Тест с картой
    assert mask_account_card("Visa Gold 1234567890123456") == "Visa Gold 1234 56** **** 3456"

    # Тест со счетом
    assert mask_account_card("Счет 12345678901234567890") == "Счет **7890"

    # Тест с другой картой
    assert mask_account_card("Maestro 9876543210987654") == "Maestro 9876 54** **** 7654"


def test_get_date():
    """Тестируем преобразование даты"""
    # Обычная дата
    assert get_date("2024-01-15T12:30:00") == "15.01.2024"

    # Другая дата
    assert get_date("2023-12-25T10:00:00") == "25.12.2023"

    # Дата с другим временем
    assert get_date("2022-07-04T18:45:30") == "04.07.2022"