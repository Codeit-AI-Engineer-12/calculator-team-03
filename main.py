import ast
import re
from random import randint

from calculator import operations
from utils.parser import parse_natural_numbers

pattern = r"\d+|//|\+\+|[+\-*/]"


def main():
    user_input = {"choice": 0, "expr": "", "point": ""}
    while user_input["choice"] != 9:
        try:
            user_input["choice"] = int(
                input(
                    "\n※ 하고픈 연산을 선택해주세요. 제발요.\n\t1. 산술연산\n\t2. 방정식\n\t3. 비교연산\n\t9. 종료\n\n\t※ 입력: "
                ).strip()
            )
        except ValueError:
            pass
        if user_input["choice"] == 1:
            print("=" * 50)
            while user_input["expr"] != "q" and user_input["expr"] != "ㅂ":
                user_input["expr"] = input(
                    "\n※ 덧셈, 뺄셈, 곱셈, 나눗셈 등을 할 수 있습니다.\n\t연산하고픈 식을 입력해주세요.\n\t뒤로 가려면 영문자 q를 입력해주세요.\n\tex) 2 + 3\n\t※ 입력: "
                )

                funny = randint(0, 9)
                if funny > 8:
                    print("아... 귀찮네... 다음에 계산할게...")
                    del funny

                a, op, b = re.findall(pattern, user_input["expr"].replace(" ", ""))
                if a == "q" or a == "ㅂ":
                    break
                if not a.isdigit():
                    print("적어도 처음은 숫자여야지")
                    continue
                a, b = parse_natural_numbers(int(a), int(b))
                if op not in operations:
                    print(f"아.. '{op}'는 연산이 안되는데..")
                if operations[op] == "++" or operations[op] == "--":
                    print(
                        "\n\t===\t", user_input["expr"], "=", operations[op](a), "\n\n"
                    )
                else:
                    print(
                        "\n\t===\t",
                        user_input["expr"],
                        "=",
                        operations[op](a, b),
                        "\n\n",
                    )

        elif user_input["choice"] == 2:
            print("1차 방정식의 기울기를 구할 수 있습니다.")
            while True:
                user_input["expr"] = input(
                    "※ 식을 입력해주세요. 이전 단계로 가려면 q를 입력하세요\n\t ex) 3x + 3\n\n\t"
                )
                if user_input["expr"].split() == "q":
                    break
                user_input["point"] = input(
                    "기울기 값을 원하는 포인트를 입력해주세요. x = "
                )

                # 숫자 뒤에 바로 영문자가 오는 경우 곱셈 연산자(*) 추가 (3x -> 3*x)
                sanitized_str = re.sub(r"(\d+)([a-zA-Z])", r"\1*\2", user_input["expr"])

                # 실행 가능한 람다 함수 형태의 문자열로 변환 ("3*x + 3" -> "lambda x: 3*x + 3")
                lambda_str = f"lambda x: {sanitized_str}"

                # AST 파싱 및 검증
                tree = ast.parse(lambda_str, mode="eval")

                if isinstance(tree.body, ast.Lambda):
                    # 컴파일 후 함수 객체 생성
                    code = compile(tree, filename="<string>", mode="eval")
                    lambda_func = eval(code)

                    # 함수 실행
                    try:
                        target_point = float(user_input["point"])
                        # 함수 정의(f, x)에 맞추어 키워드 인자로 명확하게 전달
                        result = operations["diff"](f=lambda_func, x=target_point)

                        print(
                            f"\n\t===\t x = {target_point} 에서의 기울기(근사치) = {result}\n\n"
                        )
                    except ValueError:
                        print("포인트 값에는 올바른 숫자만 입력해주세요.")
        elif user_input["choice"] == 3:
            print("아직 구현 안했지요...")
        elif (
            user_input["choice"] == 4
            or user_input["choice"] == 5
            or user_input["choice"] == 6
            or user_input["choice"] == 7
            or user_input["choice"] == 8
        ):
            print("없는 선택지에서 찾으려고 하지 마세요...쫌..")
    print("=" * 50)
    print("계산기가 종료됐습니다.")


if __name__ == "__main__":
    main()
