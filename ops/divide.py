from utils import parse_natural_numbers


def divide(a, b):

    a, b = parse_natural_numbers(a, b)
    
    if b == 0:
        return "0으로 나눌 수 없습니다."
        
    return a / b