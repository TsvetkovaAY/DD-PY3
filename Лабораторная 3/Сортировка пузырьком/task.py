from typing import Sequence


def sort(container: Sequence[int]) -> Sequence[int]:
    """
    Сортировка пузырьком

    1. Пройти по всему массиву, сравнивая каждые два соседних элемента.
    2. Если элементы не находятся в нужном порядке, меняйте их местами.
    3. Повторяйте шаг 2, пока не пройдете весь массив без изменений.
    4. Повторяйте шаги 1-3, пока не отсортируете весь массив.

    :param container: Массив, который надо отсортировать
    :return: Отсортированный в порядке возрастания массив
    """
    n = len(container)
    if n < 1:
        return container
    else:
        flag = 1
        while flag:
            cnt = 0
            n -= 1
            for i in range(n):
                if container[i] > container[i + 1]:
                    container[i], container[i + 1] = container[i + 1], container[i]
                    cnt += 1
            flag *= cnt
    return container