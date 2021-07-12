# Quesion 1.1
def multiply (m, n):
    if n != 0:
        return m + m *(n-1)

# Question 1.3
def hailstone (n):
    """Print out the hailstone sequence starting at n, and return the
    number of elements in the sequence.
    >>> a = hailstone(10)
    10
    5
    16
    8 4 2 1
    >>> a
    7
    """
    print (n)
    if n != 1 and n % 2 == 0:
        return hailstone (n / 2) + 1
    elif n != 1 and n % 2 != 0:
        return hailstone (3 * n + 1) + 1
    else: 
        return 1

# Question 1.4
def merge(n1, n2):
    """ Merges two numbers
    >>> merge(31, 42)
    4321
    >>> merge(21, 0)
    21
    >>> merge (21, 31)
    3211
    """
    if n1 == 0:
        return n2
    elif n2 == 0:
        return n1
    elif n1 % 10 < n2 % 10:
        return merge(n1 // 10, n2) * 10 + n1 % 10
    else:
        return merge(n1, n2 // 10) * 10 + n2 % 10

# Question 1.6
def is_prime(n):
    def prime_helper (k):
        if k == n:
            return True
        elif n == 1 or n % k == 0:
            return False
        else:
            return prime_helper(k+1)
    return prime_helper (2)