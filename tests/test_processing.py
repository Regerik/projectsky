from src.processing import filter_by_state, sort_by_date


def test_filter_by_state():
    data = [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
    ]

    result = filter_by_state(data)
    assert len(result) == 2
    assert result[0]['state'] == 'EXECUTED'
    assert result[1]['state'] == 'EXECUTED'

    result = filter_by_state(data, 'CANCELED')
    assert len(result) == 2
    assert result[0]['state'] == 'CANCELED'
    assert result[1]['state'] == 'CANCELED'


def test_sort_by_date():
    data = [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
    ]

    result = sort_by_date(data)
    assert result[0]['date'] == '2019-07-03T18:35:29.512364'
    assert result[1]['date'] == '2018-10-14T08:21:33.419441'

    result = sort_by_date(data, False)
    assert result[0]['date'] == '2018-06-30T02:08:58.425572'
    assert result[1]['date'] == '2018-09-12T21:27:25.241689'