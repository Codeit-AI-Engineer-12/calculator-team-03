def power(a: float, b: float) -> float:
     
     if a < 0 or b < 0:
        raise ValueError("자연수만 입력할 수 있습니다.")
        
     if a == 0 and b == 0:
        raise ValueError("0의 0제곱은 정의하지 않습니다."
     
     return a ** b