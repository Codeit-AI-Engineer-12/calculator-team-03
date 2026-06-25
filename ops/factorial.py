from utils.parser import parse_int


def factorial(n):
    """
    n! (n 팩토리얼) 값을 반환합니다.
    """

    n = parse_int(n)

    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
