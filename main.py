import re
from random import randint

from calculator import operations

MENU_CONFIG = {
    1: {
        "title": "산술 연산",
        "desc": "덧셈(+), 뺄셈(-), 곱셈(*), 나눗셈(/), 나머지(%), 거듭제곱(**) 등을 계산합니다.",
        "example": "2 + 3  또는  5 ** 2",
        "type": "binary",  # 피연산자 2개 필요
    },
    2: {
        "title": "방정식 (미분/기울기)",
        "desc": "1차 이상의 다항식을 입력하고 특정 x 포인트에서의 기울기(미분값)를 구합니다.",
        "example": "3x + 3  (x 포인트는 이후 추가 입력)",
        "type": "equation",
    },
    3: {
        "title": "수학 함수 연산",
        "desc": "팩토리얼, 최댓값, 로그 등 수학 함수 형태의 연산입니다.",
        "example": "max(10, 20)  또는  factorial(5)  또는  log(100, 10)",
        "type": "function",
    },
}


def parse_input(expr_str, mode):
    expr_str = expr_str.replace(" ", "")

    if mode == "symbol":
        # 기존 사칙연산 파싱: [숫자][연산기호][숫자]
        tokens = re.findall(r"\d+\.\d+|\d+|[\+\-\*/%]+|\*\*", expr_str)
        if len(tokens) == 3:
            return tokens[1], [int(tokens[0]), int(tokens[2])]

    elif mode == "function":
        # Case 1: 팩토리얼 후위 표기 감지 (예: 10!)
        if expr_str.endswith("!"):
            num_str = expr_str[:-1]
            if num_str.isdigit():
                return "factorial", [int(num_str)]

        # Case 2: 증감 연산자 후위 표기 감지 (예: 10++, 10--)
        if expr_str.endswith("++") or expr_str.endswith("--"):
            op = "inc" if expr_str.endswith("++") else "dec"
            num_str = expr_str[:-2]
            if num_str.replace(".", "", 1).isdigit():  # 소수점 대응
                return op, [int(num_str)]

        # Case 3: 증감 연산자 전위 표기 감지 (예: ++10, --10)
        if expr_str.startswith("++") or expr_str.startswith("--"):
            op = "inc" if expr_str.startswith("++") else "dec"
            num_str = expr_str[2:]
            if num_str.replace(".", "", 1).isdigit():
                return op, [int(num_str)]

        # Case 4: 표준 함수형 감지 (예: max(10,20), inc(5), factorial(5))
        match = re.match(r"([a-zA-Z_][a-zA-Z0-9_]*)\((.*)\)", expr_str)
        if match:
            func_name = match.group(1)
            args_str = match.group(2)
            args = [int(x) for x in args_str.split(",")] if args_str else []
            return func_name, args

    return None, []


def main():
    while True:
        print("\n" + "=" * 50)
        print("※ 하고픈 연산을 선택해주세요. 제발요.")
        for key, menu in MENU_CONFIG.items():
            print(f"\t{key}. {menu['title']}")
        print("\t9. 종료")
        print("=" * 50)

        try:
            choice = int(input("\t※ 메뉴 선택: ").strip())
        except ValueError:
            print("숫자만 입력할 수 있습니다.")
            continue

        if choice == 9:
            break
        if choice not in MENU_CONFIG:
            print("없는 선택지에서 찾으려고 하지 마세요...쫌..")
            continue

        config = MENU_CONFIG[choice]
        print(f"\n[ {config['title']} 메뉴에 진입했습니다 ]")
        print(f"설명: {config['desc']}")

        while True:
            print(f"\n* 사용법 예시: {config['example']}")
            expr = (
                input("* 식을 입력해주세요 (이전 메뉴로 가려면 'q' 입력): ")
                .strip()
                .lower()
            )

            if expr in ["q", "ㅂ"]:
                break

            if randint(0, 9) > 8:
                print("아... 귀찮네... 다음에 계산할게...")
                continue

            # --- [Case A] 방정식 메뉴 ---
            if config["type"] == "equation":
                point_input = input("* 기울기 값을 원하는 포인트를 입력해주세요. x = ")
                try:
                    target_point = float(point_input)
                    # 3x -> 3*x, x^2 -> x**2 변환
                    sanitized_str = re.sub(r"(\d+)([a-zA-Z])", r"\1*\2", expr)
                    sanitized_str = sanitized_str.replace("^", "**")
                    lambda_func = eval(f"lambda x: {sanitized_str}")

                    result = operations["diff"](f=lambda_func, x=target_point)
                    print(
                        f"\n\t===> 식 '{expr}'의 x = {target_point} 에서의 기울기 = {result}\n"
                    )
                except Exception as e:
                    print(f"오류가 발생했습니다. 식과 포인트를 다시 확인하세요. ({e})")

            # --- [Case B] 사칙연산 및 함수형 메뉴 ---
            else:
                op_or_func, args = parse_input(expr, config["type"])

                if not op_or_func or op_or_func not in operations:
                    print(
                        f"아.. 올바른 식 형식이 아니거나 '{op_or_func}' 지원하지 않는 연산입니다."
                    )
                    continue

                try:
                    # 가변 인자 처리를 위해 asterisk(*) 문법으로 리스트 해제 전달
                    result = operations[op_or_func](*args)
                    print(f"\n\t===> {expr} = {result}\n")
                except Exception as e:
                    print(f"계산 중 오류 발생: {e}")

    print("=" * 50)
    print("계산기가 완전히 종료됐습니다. 고생하셨습니다. 근데 연산은 제가 했습니다.")


if __name__ == "__main__":
    main()
