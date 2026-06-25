from utils.parser import parse_natural_numbers


def multiply(a: int, b: int) -> int | None:
    """int형 두 수를 곱합니다

    Args:
        a (int): int형 숫자
        b (int): int형 숫자

    Returns:
        int: a와 b를 곱한 값
        None: a나 b가 정상적인 값이 아닐 경우
    """
    a, b = parse_natural_numbers(a, b)
    return a * b
