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


def sort_by_date(list_of_dicts: list, reverse_order: bool = True) -> list:
    """
    Сортирует список словарей по дате

    Аргументы:
        list_of_dicts: список словарей с данными операций
        reverse_order: порядок сортировки (True - убывание, False - возрастание)

    Возвращает:
        Новый отсортированный список
    """
    return sorted(list_of_dicts, key=lambda x: x['date'], reverse=reverse_order)
