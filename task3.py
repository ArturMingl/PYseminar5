"""
Создайте функцию генератор чисел Фибоначчи
"""


def fib_gen():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


if __name__ == "__main__":
    fib = fib_gen()
    for __ in range(15):
        print(next(fib))
