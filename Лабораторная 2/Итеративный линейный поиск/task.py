"""
This module implements some functions based on linear search algo
"""
from typing import List


def min_search(arr: List[int]) -> int:
    """
    Функция для поиска минимума в массиве

    :param arr: Массив целых чисел
    :return: Индекс первого вхождения элемента в массиве
    """
    len_ = len(arr)

    if len_ <= 0:
        raise ValueError()

    min_ = arr[0]
    index_min = 0

    for i in range(1, len_):
        if arr[i] < min_:
            min_ = arr[i]
            index_min = i
    return index_min
