from typing import TextIO


def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total
print("Hello")
print(multiply(2,3,4,5))
