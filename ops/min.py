from utils.parser import parse_natural_numbers


def min(a: int, b: int) -> int:
    """두 수 중 더 적은 값을 반환

    Args:
        a (int): int형 숫자
        b (int): int형 숫자

    Returns:
        int: 작은 수를 반환합니다
    """
    a, b = parse_natural_numbers(a, b)
    if a < 0 or b < 0:
        return 0
    return min(a, b)
