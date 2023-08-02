# импорт функций из файла utils
from utils import get_all_operations, sort_by_date, get_formated_operation, filter_five_by_executed

# получаем операции из json файла
data_file = get_all_operations("operations.json")
# сортируем по дате
sorted_file = sort_by_date(data_file)
# фильтр успешной транзакции и вывод 5 транзакций
filtered = filter_five_by_executed(sorted_file)
# цикл по 5 транзакциям и принт
for operation in filtered:
    print(get_formated_operation(operation))
