from utils.parser import parse_natural_numbers


def divide(a, b):
    """
    두 자연수를 나누는 함수입니다.

    Args:
        a (int): 나뉘어지는 수
        b (int): 나누는 수 (0이 아니어야 함)

    Returns:
        float or str: 나눗셈 결과값, 또는 0으로 나눌 경우의 에러 메시지
    """

    a, b = parse_natural_numbers(a, b)
    
    if b == 0:
        return "0으로 나눌 수 없습니다."
        
    return a / b