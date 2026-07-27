"""
Тесты для модуля masks
"""

from src.masks import get_mask_card_number, get_mask_account


def test_get_mask_card_number():
    """Тестируем маскировку номера карты"""
    # Обычный номер карты
    assert get_mask_card_number("1234567890123456") == "1234 56** **** 3456"

    # Номер карты с пробелами (их удалять не нужно, функция работает с чистой строкой)
    assert get_mask_card_number("1234567890123456") == "1234 56** **** 3456"

    # Другой номер карты
    assert get_mask_card_number("9876543210987654") == "9876 54** **** 7654"


def test_get_mask_account():
    """Тестируем маскировку номера счета"""
    # Обычный номер счета
    assert get_mask_account("12345678901234567890") == "**7890"

    # Другой номер счета
    assert get_mask_account("98765432109876543210") == "**3210"