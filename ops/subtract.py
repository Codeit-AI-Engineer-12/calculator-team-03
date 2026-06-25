from utils.parser import parse_natural_numbers


def subtract(a=None, b=None):
    a, b = parse_natural_numbers(a, b)
    return a - b
