def mod(a: int, b: int) -> int:
    """큰 수에서 작은 수를 나눈 나머지를 계산합니다.

    Args:
        a (int): int형 숫자
        b (int): int형 숫자

    Returns:
        int: 큰 수에서 작은 수를 나눈 나머지를 반환합니다.
    """
    return max(a, b) % min(a, b)
