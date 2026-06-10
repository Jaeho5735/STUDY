# [실습 1] Persona & Structure
# 목표: 절차지향 코드를 "객체지향(OOP) + SOLID 원칙"이 적용된 구조로 변경하세요.
# Bad Prompt: "이거 리팩토링해줘" (단순 함수화)
# Good Prompt: "너는 SW 아키텍트야. 추상 클래스(ABC)를 사용하여 확장 가능한 구조로 바꾸고, SOLID 원칙을 적용해줘."

op = input("연산자(+, -, *, /): ")
n1 = int(input("숫자1: "))
n2 = int(input("숫자2: "))

if op == '+':
    print(n1 + n2)
elif op == '-':
    print(n1 - n2)
elif op == '*':
    print(n1 * n2)
elif op == '/':
    if n2 == 0:
        print("에러")
    else:
        print(n1 / n2)
