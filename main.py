import re
from random import randint

from calculator import operations
from utils.parser import parse_natural_numbers

pattern = r"\d+|//|\+\+|[+\-*/]"


def main():
    user_input = {"choice": 0, "expr": ""}
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

    print("=" * 50)
    print("계산기가 종료됐습니다.")


if __name__ == "__main__":
    main()
