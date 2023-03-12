def check_brackets(brackets_row: str) -> bool:
    """
    Проверьте, является ли входная строка допустимой последовательностью скобок

    :param brackets_row: Входная строка для проверки
    :return: True, если последовательность корректна, False в противном случае
    """
    list_brackets = list(brackets_row)
    print(list_brackets)

    stack = []

    len_ = len(list_brackets)
    if len_ == 0:
        return True

    for i in range(len_):
        if list_brackets[i] == '(':
            stack.append("(")
        else:
            if stack:
                stack.pop()
            else:
                return False
    if len(stack) == 0:
        return True
    else:
        return False


if __name__ == '__main__':
    print(check_brackets("()()"))  # True
    print(check_brackets(")("))  # False
