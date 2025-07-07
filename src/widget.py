from datetime import datetime
from src.masks import get_mask_card_number, get_mask_account


def mask_account_card(data: str) -> str:
    """
    Возвращает строку с замаскированным номером
    """
    last_space = data.rfind(" ")
    if "Счет" in data[:last_space]:
        return data[:last_space] + " " + get_mask_account(data[last_space + 1:])
    else:
        return data[:last_space] + " " + get_mask_card_number(data[last_space + 1:])


def get_date(date_str: str) -> str:
    """
    Форматирует дату в формат "ДД.ММ.ГГГГ"
    """
    date_obj = datetime.fromisoformat(date_str)
    return date_obj.strftime("%d.%m.%Y")
