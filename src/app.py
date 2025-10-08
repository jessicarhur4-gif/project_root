# src/app.py
import argparse

def greet(name: str) -> str:
    return f"Hello, {name}!"

def safe_int(x):
    try:
        return int(x)
    except (ValueError, TypeError):
        return 0

def add(a, b):
    return safe_int(a) + safe_int(b)

def main():
    parser = argparse.ArgumentParser(description="Simple CLI App")
    parser.add_argument("--name", default="Git", help="Your name")
    parser.add_argument("--a", default=0, help="first number")
    parser.add_argument("--b", default=0, help="second number")
    args = parser.parse_args()

    print(greet(args.name))
    print(f"{args.a} + {args.b} = {add(args.a, args.b)}")

if __name__ == "__main__":
    main()