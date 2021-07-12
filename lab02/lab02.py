# Question 3
def lambda_curry2(func):
    """
    Returns a Curried version of a two-argument function FUNC.
    >>> from operator import add, mul, mod
    >>> curried_add = lambda_curry2(add)
    >>> add_three = curried_add(3)
    >>> add_three(5)
    8
    >>> curried_mul = lambda_curry2(mul)
    >>> mul_5 = curried_mul(5)
    >>> mul_5(42)
    210
    >>> lambda_curry2(mod)(123)(10)
    3
    """
    return lambda x: lambda y: func(x,y)
# Question 4
def count_cond(condition):
    def counting(n):
        i, count = 1, 0
        while i <= n:
            if condition (n, i) == True:
                count += 1
            i = i + 1
        return count
    return lambda n: counting(n)

# Question 7
def composite_identity(f, g):
    def compose(x):
        if f(g(x)) == g(f(x)):
            return True
        else:
            return False
    return lambda x: compose(x)

# Question 8
def cycle(f1, f2, f3):
    def func(n):
        def g(x):
            i = 1
            floor = n // 3
            mod = n % 3
            function = lambda x: f3(f2(f1(x)))
            def f(x):
                if floor == 0:
                    return x
                else:
                    while i < floor:
                        function = f3(f2(f1(function(x))))
                        i = i + 1
                return function(x)
            if mod == 1:
                return f1(f(x))
            elif mod == 2:
                return f2(f1(f(x)))
            else:
                return f(x)
        return g
    return func