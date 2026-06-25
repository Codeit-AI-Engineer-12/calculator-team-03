from utils.parser import parse_natural_numbers


def root(a=None, b=None):
    """
    두 자연수의 제곱근을 반환합니다.

    Args:
        a (int): 밑이 되는 자연수
        b (int): 지수가 되는 자연수

    Returns:
        float: 두 자연수의 제곱근

    Raises:
        ValueError: 입력이 없거나, 자연수가 아니면 발생합니다.
    """
    a, b = parse_natural_numbers(a, b)
    if b == 0:
        raise ValueError("지수는 0이 될 수 없습니다.")
    return a ** (1 / b)
