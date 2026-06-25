from ops.parser import parse_natural_numbers


def add(a=None, b=None):
    """두 자연수의 합을 반환합니다.

    Args:
        a (int): 첫 번째 자연수
        b (int): 두 번째 자연수

    Returns:
        int: 두 자연수의 합

    Raises:
        ValueError: 입력이 없거나, 자연수가 아니면 발생합니다.
    """
    a, b = parse_natural_numbers(a, b)
    return a + b
