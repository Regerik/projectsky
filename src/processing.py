def filter_by_state(list_of_dicts: list, state: str = 'EXECUTED') -> list:
    """
    Фильтрует список словарей по значению ключа 'state'

    Аргументы:
        list_of_dicts: список словарей с данными операций
        state: значение для фильтрации (по умолчанию 'EXECUTED')

    Возвращает:
        Новый список словарей с указанным статусом
    """
    filtered_list = []
    for item in list_of_dicts:
        if item.get('state') == state:
            filtered_list.append(item)
    return filtered_list