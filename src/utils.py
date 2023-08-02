# импорт модуоя json
import json


def get_all_operations(file):
    """
     получает список из json файла
    :param file:
    :return:
    """
    with open(file) as data_file:
        operations = json.load(data_file)
    return operations


def sort_by_date(operations):
    """
    добавляет в пустой список отсортированные по дате транзакции
    :param operations:
    :return:
    """
    valid_operations = []
    for operation in operations:
        if not operation:
            continue
        elif not 'date' in operation:
            continue
        elif not operation.get('date'):
            continue
        valid_operations.append(operation)

    sorted_data = sorted(valid_operations, key=lambda operation: operation['date'], reverse=True)
    return sorted_data


def filter_five_by_executed(sorted_data):
    """
    фильтрует по значению "EXECUTED" и добавляет 5 последних транзакций
    :param sorted_data:
    :return:
    """
    executed_operations = []
    for operation in sorted_data:
        if operation['state'] == "EXECUTED":
            executed_operations.append(operation)
        if len(executed_operations) == 5:
            return executed_operations


def get_formated_operation(operation):
    """
    преобразует вывод транзакций в консоль
    :param operation:
    :return:
    """
    # первая строчка принта
    line_1 = ""
    # отсекает вторую часть даты
    date_raw = operation['date'][:10]
    slice_date = date_raw.split('-')
    # зеркалит дату через точку
    my_date = '.'.join(reversed(slice_date))
    line_1 = my_date + " "
    line_1 += operation['description']

    line_2 = ""
    # условие по транзакции
    from_info = operation.get('from')
    if from_info:
        hidden_info = mask_number(from_info)
        line_2 += hidden_info
    to_info = operation['to']
    hidden_to_info = mask_number(to_info)
    # line_2 += hidden_to_info

    return f"{line_1}\n" \
           f"{line_2} -> {hidden_to_info}\n" \
           f"{operation['operationAmount']['amount']} {operation['operationAmount']['currency']['name']}\n"


def mask_number(bill_info):
    """
    маскирует номер карты или счета
    :param bill_info:
    :return:
    """
    # берем последний элемент
    card_info = bill_info.split()
    number = card_info[-1]
    # условие маскировки счета или карты
    if bill_info.lower().startswith("счет"):
        masked_number = f"**{number[-4:]}"
    else:
        masked_number = f"{number[:4]} {number[4:6]}** **** {number[-4:]}"
    card_info[-1] = masked_number
    hidden_bill_info = ' '.join(card_info)
    return hidden_bill_info
