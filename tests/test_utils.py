from src import utils


def test_get_all_operations():

    assert utils.get_all_operations("../src/test.json") == [
        {"id": 441945886, "state": "EXECUTED", "date": "2019-08-26T10:50:58.294041"}]


def test_sort_by_date():
    test_operations = [
        {"state": "EXECUTED",
         "date": "2018-08-26T10:50:58.294041",
         },
        {"state": "EXECUTED",
         "date": "2019-08-26T10:50:58.294041",
         }
    ]
    expected = [
        {"state": "EXECUTED",
         "date": "2019-08-26T10:50:58.294041",
         },
        {"state": "EXECUTED",
         "date": "2018-08-26T10:50:58.294041",
         }
    ]
    assert utils.sort_by_date(test_operations) == expected


def test_filter_five_by_executed():
    test_sort_operations = [
        {"state": "EXECUTED",
         "date": "2019-08-26T10:50:58.294041",
         },
        {"state": "EXECUTED",
         "date": "2018-08-26T10:50:58.294041",
         },
        {"state": "EXECUTED",
         "date": "2017-08-26T10:50:58.294041",
         },
        {"state": "EXECUTED",
         "date": "2016-08-26T10:50:58.294041",
         },
        {"state": "EXECUTED",
         "date": "2019-08-26T10:50:58.294041",
         },
        {"state": "EXECUTED",
         "date": "2015-08-26T10:50:58.294041",
         },
        {"state": "EXECUTED",
         "date": "2014-08-26T10:50:58.294041",
         }
    ]
    test_five_operation = [
        {"state": "EXECUTED",
         "date": "2019-08-26T10:50:58.294041",
         },
        {"state": "EXECUTED",
         "date": "2018-08-26T10:50:58.294041",
         },
        {"state": "EXECUTED",
         "date": "2017-08-26T10:50:58.294041",
         },
        {"state": "EXECUTED",
         "date": "2016-08-26T10:50:58.294041",
         },
        {"state": "EXECUTED",
         "date": "2019-08-26T10:50:58.294041",
         }
    ]
    assert utils.filter_five_by_executed(test_sort_operations) == test_five_operation


def test_get_formated_operation():
    test_operation = {'id': 154927927, 'state': 'EXECUTED', 'date': '2019-11-19T09:22:25.899614',
                      'operationAmount': {'amount': '30153.72', 'currency': {'name': 'руб.', 'code': 'RUB'}},
                      'description': 'Перевод организации', 'from': 'Maestro 7810846596785568',
                      'to': 'Счет 43241152692663622869'}
    print_info = "19.11.2019 Перевод организации\nMaestro 7810 84** **** 5568 -> Счет **2869\n30153.72 руб.\n"

    assert utils.get_formated_operation(test_operation) == print_info


def test_mask_number():
    test_card = "Maestro 7810846596785568"
    test_bill = "Счет 43241152692663622869"
    assert utils.mask_number(test_card) == "Maestro 7810 84** **** 5568"
    assert utils.mask_number(test_bill) == "Счет **2869"
