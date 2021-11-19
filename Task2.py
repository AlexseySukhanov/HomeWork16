from datetime import datetime

def fibo():
    """
    Wrapped memorized function calculates Fibonacci number
    :return: Fibonacci number of n elements
    """
    result = {}
    a = 0
    b = 1
    def wrap(n):
        nonlocal result
        nonlocal a
        nonlocal b
        if result.get(n):
            return result.get(n)
        else:
            for i in range(3,n+1):
                a, b = b, a + b
            return b
    return wrap

def fibo_rec(n : int) -> int:
    """
    Recursion function calculates Fibonacci number
    :param n Number of Fibonacci elements:
    :return: Fibonacci number of n elements
    """
    if n in (1, 2):
        return 1
    return fibo_rec(n - 1) + fibo_rec(n - 2)

start_rec = datetime.now()
print(fibo_rec(40))
stop_rec = datetime.now()

start_wrap = datetime.now()
numbers = fibo()
print(numbers(40))
stop_wrap = datetime.now()

print(f'Wrapped function complited in {stop_wrap-start_wrap}\n'
      f'Recursion function complited in {stop_rec-start_rec} ')
