
__all__ = ['my_sum']


def my_sum(iterable):
    tot = 0
    for i in iterable:
        tot += i
    return tot

@cache
def factorial(n):
    return n * factorial(n-1) if n else 1

@cache
def sin(x):
    coeff = (-1)**n/factorial(2*n+1)
    return my_sum(coeff*(x**(2*n+1)))