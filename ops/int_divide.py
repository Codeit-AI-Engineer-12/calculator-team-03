def int_divide(a, b):
    """
    두 자연수 a와 b를 입력받아 a를 b로 정수 나눗셈한 몫을 반환합니다.
    """
    if b == 0:
        raise ValueError("0으로 나눌 수 없습니다.")

    return a // b
