def parse_natural_numbers(a, b):
    """자연수 입력인지 검증하고, 두 값을 반환합니다.

    Args:
        a: 첫 번째 입력값
        b: 두 번째 입력값

    Returns:
        tuple[int, int]: 검증된 자연수 두 개

    Raises:
        ValueError: 입력이 없거나, 불리언이거나, 정수가 아니거나, 음수이면 발생합니다.
    """
    if a is None or b is None:
        raise ValueError("a and b are required")

    if isinstance(a, bool) or isinstance(b, bool):
        raise ValueError("boolean values are not allowed")

    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("a and b must be integers")

    if a < 0 or b < 0:
        raise ValueError("a and b must be natural numbers")

    return a, b
