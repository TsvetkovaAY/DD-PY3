def factorial_recursive(n: int) -> int:
    """
    Рассчитать факториал числа n рекурсивным способом

    :param n: Число, факториал которого нужно найти
    :return: n! - факториал числа n
    """
    if not isinstance(n, int):
        raise TypeError()
    if n < 0:
        raise ValueError
    elif n == 0:
        return 1
    else:
        factorial = factorial_recursive(n - 1) * n
    return factorial
