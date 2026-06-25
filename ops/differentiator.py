def differentiator(f, x, h=1e-7):
    """
    수치 미분을 계산하는 함수입니다.
    Args:
        f (callable): 미분할 함수
        x (float): 미분을 계산할 점
        h (float, optional): 미분 계산에 사용할 작은 값. 기본값은 1e-7입니다.
    Returns:
        float: f의 x에서의 근사 미분값
    Raises:
        ValueError: x가 숫자가 아니거나, boolean인 경우 발생합니다.
    usage:
        >>> differentiator(f = lambda x: x**2, 3)
        6.000000000838668
    """
    if not isinstance(x, (int, float)):
        raise ValueError("숫자(int 또는 float)만 입력 가능합니다.")
    if isinstance(x, bool):
        raise ValueError("boolean은 입력할 수 없습니다.")

    return (f(x + h) - f(x - h)) / (2 * h)
