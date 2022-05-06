#!/usr/bin/python3

import sys


def fizz_buzz(i: int) -> str:    
    
    fizz = "Fizz" if i%3==0 else ""
    buzz = "Buzz" if i%5==0 else ""

    if any([fizz, buzz]):
        return f"{fizz}{buzz}!"
    else:
        return f"Number: {i}"


def main():
    sys.stdout.write("""Welcome to Fizz Buzz!
Submit a number and get an answer""")

    for num in range(1, 101):
        res = fizz_buzz(num) + "\n"

        sys.stdout.write(res)


if __name__ == "__main__":
    main()
