from combination import combination


def combination_with_repetition(n, r):
    """
    n개의 항목 중 r개를 선택하는 조합(중복 허용)을 계산하는 함수입니다.

    Args:
        n (int): 전체 항목의 수
        r (int): 선택할 항목의 수

    Returns:
        int: 조합(중복 허용)의 결과값
    Raises:
        ValueError: n또는 r이 음수인 경우
    """
    if n < 0 or r < 0:
        raise ValueError(
            "Invalid values for n and r. Ensure that n and r are non-negative."
        )

    return combination(n + r - 1, r)
