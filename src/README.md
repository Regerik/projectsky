Проект для обработки данных банковских операций.

# Банковские операции

Учебный проект для обработки данных банковских операций.

## Функции

- `mask_account_card()` - маскирует номер карты или счета
- `get_date()` - преобразует дату в формат ДД.ММ.ГГГГ
- `filter_by_state()` - фильтрует операции по статусу
- `sort_by_date()` - сортирует операции по дате

## Пример использования

```python
from src.widget import mask_account_card, get_date
from src.processing import filter_by_state, sort_by_date

# Маскировка
print(mask_account_card("Visa Gold 1234567890123456"))
# Результат: Visa Gold 1234 56** **** 3456

# Дата
print(get_date("2024-01-15T12:30:00"))
# Результат: 15.01.2024

# Фильтрация
operations = [
    {'id': 1, 'state': 'EXECUTED', 'date': '2024-01-10'},
    {'id': 2, 'state': 'CANCELED', 'date': '2024-01-11'}
]
print(filter_by_state(operations))

## Тестирование

Запуск тестов:

pytest

## Отчет о покрытии

pytest --cov=src --cov-report=html

После выполнения откройте htmlcov/index.html в браузере.

