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


def parse_numbers(
    nums: int | float | list[int | float], except_negative=False
) -> list[int | float]:
    """배열을 받아 숫자 배열로 반환합니다.

    Args:
        nums (list[int  |  float]): 숫자 배열
        except_negative (bool, optional): 음수를 제외할지 정합니다. Defaults to False.

    Returns:
        list[int | float]: 숫자 배열을 반환하거나 배열 중 하나라도 숫자가 아닐 경우 [-inf] 을 반환합니다
    """
    if isinstance(nums, (int, float)):
        nums = [nums]

    processed_result = []

    for val in nums:
        if val is None:
            return [float("-inf")]
        elif not isinstance(val, (int, float)):
            return [float("-inf")]

        elif isinstance(val, str):
            try:
                num = float(val)
                # 소수점 아래가 없는 깔끔한 숫자(예: 4.0)는 int로 변환
                val = int(num) if num.is_integer() else num
            except ValueError:
                # 숫자로 바꿀 수 없는 문자열이면 즉시 실패
                return [float("-inf")]

        if except_negative and val < 0:
            return [float("-inf")]

        # 모든 검증을 통과한 값만 저장
        processed_result.append(val)

    return processed_result


def parse_int(num: str | float | int) -> int:
    """문자열 혹은 정수, 실수를 받아 정수로 반환합니다.

    Args:
        num (str | float | int): 숫자인 문자열, 정수, 실수

    Returns:
        int: 어떤 값이든 정수로 반환합니다. 다만 숫자가 아닌 문자열은 0을, 실수는 소수점을 버리고 반환
    """
    if isinstance(num, str) and num.isdigit():
        return int(num)
    elif isinstance(num, float):
        return int(num)
    elif isinstance(num, int):
        return num
    return 0
