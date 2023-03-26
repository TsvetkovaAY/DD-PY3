from typing import Sequence


def sort(container: Sequence[int]) -> Sequence[int]:
    """
    Сортировка подсчетами

    1. Определите максимальное значение в массиве и заполните вспомогательный массив с подсчетом количества элементов.
    2. Посчитайте количество каждого объекта
    3. Зная количество каждого объекта, восстановите отсортированный массив

    :param container: Массив, который надо отсортировать
    :return: Отсортированный в порядке возрастания массив
    """
    n = len(container)
    if n <= 1:
        return container
    max_ = max(container)
    mas = [0] * (max_ + 1)  # создали вспомогательным массив с нулями
    for val in container:  # заполнили вспомогательный массив
        mas[val] += 1
    container = [0] * n
    k = 0
    for i in range(len(mas)):
        while mas[i] != 0:
            container[k] = i
            k += 1
            mas[i] -= 1
    return container
