from utils.parser import parse_natural_numbers


def max_num(a, b):
    """
    두 자연수 중 더 큰 값을 반환합니다.

    Args:
        a (int): 비교할 자연수
        b (int): 비교할 자연수

    Returns:
        int: 더 큰 값
    """
    a, b = parse_natural_numbers(a, b)

    # 파이썬 내장 max() 활용
    return max(a, b)
