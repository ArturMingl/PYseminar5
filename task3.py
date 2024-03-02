"""
Создайте функцию генератор чисел Фибоначчи
"""

def fib(n: int) -> list[int]:
    a, b = 0, 1
    for __ in range(n):
        yield a
        a, b = b, a + b

if __name__ == "__main__":
    for num in fib(15):
        print(num)
