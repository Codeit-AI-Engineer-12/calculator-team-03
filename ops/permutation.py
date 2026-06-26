from ops.factorial import factorial


def permutation(n, r):
    """
    n개의 항목 중 r개를 선택하는 순열을 계산하는 함수입니다.

    Args:
        n (int): 전체 항목의 수
        r (int): 선택할 항목의 수

    Returns:
        int: 순열의 결과값
    Raises:
        ValueError: n또는 r이 음수이거나 r이 n보다 큰 경우
    """
    if r > n or n < 0 or r < 0:
        raise ValueError("Invalid values for n and r. Ensure that 0 <= r <= n.")

    return factorial(n) // factorial(n - r)
