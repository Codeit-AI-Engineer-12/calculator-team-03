import math
from utils.parser import parse_natural_numbers

def log(a, b):
    """
    b를 밑으로 하는 a의 로그 값을 반환합니다. (log_b(a))

    Args:
        a (int): 진수 (a > 0 이어야 함)
        b (int): 밑 (b > 0 이고, b != 1 이어야 함)

    Returns:
        float or str: 로그 계산 결과, 또는 조건 불만족 시 에러 메시지
    """
    a, b = parse_natural_numbers(a, b)

    # 로그의 수학적 조건 방어 (파서는 0을 통과시키므로 직접 막아야 합니다)
    if a <= 0:
        return "진수(a)는 양수여야 합니다."
    if b <= 0 or b == 1:
        return "밑(b)은 1이 아닌 양수여야 합니다."

    return math.log(a, b)