def num_eights(x):
    """Returns the number of times 8 appears as a digit of x.

    >>> num_eights(3)
    0
    >>> num_eights(8)
    1
    >>> num_eights(88888888)
    8
    >>> num_eights(2638)
    1
    >>> num_eights(86380)
    2
    >>> num_eights(12345)
    0
    >>> from construct_check import check
    >>> # ban all assignment statements
    >>> check(HW_SOURCE_FILE, 'num_eights',
    ...       ['Assign', 'AugAssign'])
    True
    """
    if x == 0:
        return 0
    elif x % 10 == 8:
        return 1 + num_eights(x // 10)
    else:
        return num_eights(x // 10)

def num_eights(x):
     if x == 0:
        return 0
    elif x % 10 == 8:
        return 1 + num_eights(x // 10)
    else:
        return num_eights(x // 10)

def nums_contains_eights(n):
    if n < 18:
        return 0
    elif n // 8 !=0 and num_eights(n) != 0:
        return 1 + nums_contains_eights(n-1)
    else: 
        return nums_contains_eights(n-1)

def pingpong(n):
    if n == 1:
        return 1
    elif ((n-1) // 8 + nums_contains_eights (n-1)) % 2 != 0:
        return pingpong(n-1) - 1
    else:
        return pingpong(n-1) + 1

def missing_digits(n):
    if n // 10 < 1:
        return 0
    elif n % 10 - (n // 10) % 10 >= 2:
        return  1 + missing_digits(n // 10)
    else:
        return missing_digits(n // 10)

def next_largest_coin(coin):
    if coin == 1:
        return 5
    elif coin == 5:
        return 10
    elif coin == 10:
        return 25

def count_coins(total):
    def count(total, coin):
        if total == 0:
            return 1
        elif total < 0:
            return 0
        elif next_largest_coin(coin) == None:
            return 0
        else:
            return count(total-coin, coin) + count(total, next_largest_coin(coin))
    return count(total, 1)

from operator import sub, mul

def make_anonymous_factorial():
    """Return the value of an expression that computes factorial.

    >>> make_anonymous_factorial()(5)
    120
    >>> from construct_check import check
    >>> # ban any assignments or recursion
    >>> check(HW_SOURCE_FILE, 'make_anonymous_factorial', ['Assign', 'AugAssign', 'FunctionDef', 'Recursion'])
    True
    """
    return (lambda f: lambda k: f(f, k))(lambda f, k: k if k == 1 else k * f(f, k-1))