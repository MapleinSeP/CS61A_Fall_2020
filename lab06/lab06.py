this_file = __file__


def make_adder_inc(a):
    """
    >>> adder1 = make_adder_inc(5)
    >>> adder2 = make_adder_inc(6)
    >>> adder1(2)
    7
    >>> adder1(2) # 5 + 2 + 1
    8
    >>> adder1(10) # 5 + 10 + 2
    17
    >>> [adder1(x) for x in [1, 2, 3]]
    [9, 11, 13]
    >>> adder2(5)
    11
    """
    c = 0
    def f(b):
        nonlocal c
        c = c + 1
        return a + b + c - 1
    return f


def make_fib():
    """Returns a function that returns the next Fibonacci number
    every time it is called.

    >>> fib = make_fib()
    >>> fib()
    0
    >>> fib()
    1
    >>> fib()
    1
    >>> fib()
    2
    >>> fib()
    3
    >>> fib2 = make_fib()
    >>> fib() + sum([fib2() for _ in range(5)])
    12
    >>> from construct_check import check
    >>> # Do not use lists in your implementation
    >>> check(this_file, 'make_fib', ['List'])
    True
    """
    n = 0
    def f():
        nonlocal n
        n = n + 1
        f = 0
        f1 = 0
        f2 = 1
        i = 2
        if n == 1:
            return f1
        elif n == 2:
            return f2
        else:
            while i <= n:
                f = f1 + f2
                f2 = f1
                f1 = f
                i = i + 1
            return f
    return f

"""
None

[5, 6, 7, 8, 6]

[9 ,5, 6, 7, 8, 6]

[9 ,5, 7, 8, 6]

[9 ,5, 7, 8]

Yes

Yes

False
"""

def insert_items(lst, entry, elem):
    """
    >>> test_lst = [1, 5, 8, 5, 2, 3]
    >>> new_lst = insert_items(test_lst, 5, 7)
    >>> new_lst
    [1, 5, 7, 8, 5, 7, 2, 3]
    >>> large_lst = [1, 4, 8]
    >>> large_lst2 = insert_items(large_lst, 4, 4)
    >>> large_lst2
    [1, 4, 4, 8]
    >>> large_lst3 = insert_items(large_lst2, 4, 6)
    >>> large_lst3
    [1, 4, 6, 4, 6, 8]
    >>> large_lst3 is large_lst
    True
    """
    i = 0
    while i <= len(lst) - 1:
        if lst[i] == entry:
            lst.insert(i + 1, elem)
            i = i + 2
        else:
            i = i + 1
    return lst

