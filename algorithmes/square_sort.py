# Задача: отсортировать список [2, 4, 1, 3, 5] по возрастанию -> [1, 2, 3, 4, 5]
# Квадратичные сортировки - O(N ** 2)

# соритровка вставками (insert sort)
def insert_sort(a):
    """ сортировка списка a вставками
    :param a: массив
    :return: сортированный массив
    """
    for top in range(1, len(a)):
        k = top
        while k > 0 and a[k - 1] > a[k]:
            a[k], a[k - 1] = a[k - 1], a[k]
            k -= 1


# сортировка методом выбора (choice sort)
# объявляется "вакантная позиция" в которую складывается элемент < текущего
# цикл идет до конца массива
# следующая "вакантная позиция передвигается на 1"
def choice_sort(a):
    """ сортировка выбором
    :param a: массив
    :return: сортированный массив
    """
    pass


# пузырьковая сортировка (bubble sort)
# сравнивает 2 элемента списка
# если 1 > 2, то оставляет все на месте
# если 2 > 1, меняет элементы местами
# сдвигается текущая позиция
def bubble_sort(a):
    """ пузырьковая сортировка
    :param a: массив
    :return: сортированный массив
    """
    pass


def test_sort(sorting_algorithm):
    print('Тестируем: ' + sorting_algorithm.__doc__)
    array = [3, 2, 4, 1, 5]
    sorted_array = [1, 2, 3, 4, 5]
    sorting_algorithm(array)
    print('test1 passed' if array == sorted_array else 'test1 did not passed')

    array = list(range(10, 20)) + list(range(10))
    sorted_array = list(range(20))
    sorting_algorithm(array)
    print('test2 passed' if array == sorted_array else 'test2 did not passed')

    array = [-10, 0, -1000, 10, 1000]
    sorted_array = [-1000, -10, 0, 10, 1000]
    sorting_algorithm(array)
    print('test3 passed' if array == sorted_array else 'test3 did not passed')
    print('\n\n')


if __name__ == '__main__':
    test_sort(insert_sort)
    test_sort(choice_sort)
    test_sort(bubble_sort)
