# src/app.py

import argparse

# 이름을 받아 인사하는 함수
def greet(name: str) -> str:
    return f"Hello, {name}!"

# 안전하게 정수로 변환하는 함수
def safe_int(value):
    try:
        return int(value)
    except ValueError:
        return 0

# 두 수를 더하는 함수
def add(a, b):
    return safe_int(a) + safe_int(b)

# 프로그램의 시작점
def main():
    parser = argparse.ArgumentParser(description="Simple Python CLI App using Git")
    parser.add_argument("--name", default="GitHub", help="이름을 입력하세요")
    parser.add_argument("--a", default=0, help="첫 번째 숫자")
    parser.add_argument("--b", default=0, help="두 번째 숫자")
    args = parser.parse_args()

    print(greet(args.name))
    print(f"{args.a} + {args.b} = {add(args.a, args.b)}")

if __name__ == "__main__":
    main()