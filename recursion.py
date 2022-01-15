import sys
sys.setrecursionlimit(100000)


def factorial(n):
    assert n >= 0 and int(n) == n, 'n must be a non-negative integer'
    if n in [0, 1]:
        return 1
    else:
        return n * factorial(n-1)

# print(factorial(5))


def fibonacci(n):
    assert n >= 0 and int(n) == n, 'n must be a non-negative integer'
    if n in [0, 1]:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# print(fibonacci(6))


def sum_of_digits(n):
    assert n >= 0 and int(n) == n, 'n must be a non-negative integer'
    if n in [0]:
        return n
    else:
        return n % 10 + sum_of_digits(n // 10)

# print(sum_of_digits(12345))


def power(n, p):
    assert p >= 0 and int(p) == p, 'p must be a non-negative integer'
    if n < 0:
        n = abs(n)
        pass
    if p == 0:
        return 1
    if n == 1:
        return n
    else:
        return n * power(n, p-1)


print(power(-2,3))
