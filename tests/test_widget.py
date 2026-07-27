"""
Тесты для модуля widget
"""

import pytest
from src.widget import mask_account_card, get_date


@pytest.mark.parametrize("input_data, expected", [
    ("Visa Gold 1234567890123456", "Visa Gold 1234 56** **** 3456"),
    ("Счет 12345678901234567890", "Счет **7890"),
    ("Maestro 9876543210987654", "Maestro 9876 54** **** 7654"),
    ("Мир 1111222233334444", "Мир 1111 22** **** 4444")
])
def test_mask_account_card(input_data, expected):
    assert mask_account_card(input_data) == expected


@pytest.mark.parametrize("date_str, expected", [
    ("2024-01-15T12:30:00", "15.01.2024"),
    ("2023-12-25T10:00:00", "25.12.2023"),
    ("2022-07-04T18:45:30", "04.07.2022")
])
def test_get_date(date_str, expected):
    assert get_date(date_str) == expected