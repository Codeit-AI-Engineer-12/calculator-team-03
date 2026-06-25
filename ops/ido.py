from utils.parser import parse_natural_numbers


def increase(num: int, step: int = 1, count: int = 1) -> int:
    """덧셈과 같은 연산(Advanced)

    Args:
        num (int): 원래 숫자
        step (int, optional): 더할 수. Defaults to 1.
        count (int, optional): 몇 번 더할지. Defaults to 1.

    Returns:
        int: num 에 step을 count번 더한 값을 반환.
            step을 지정하지 않을 시 1을 한 번 더한 값을 반환
    """
    num, step = parse_natural_numbers(num, step)

    return num + step * count


def decrease(num: int, step: int = 1, count: int = 1):
    """뺄셈과 같은 연산(Advanced)

    Args:
        num (int): 원래 숫자
        step (int, optional): 뺄 수. Defaults to 1.
        count (int, optional): 몇 번 뺄지. Defaults to 1.

    Returns:
        _type_: _description_
    """
    num, step = parse_natural_numbers(num, step)

    return num - step * count
