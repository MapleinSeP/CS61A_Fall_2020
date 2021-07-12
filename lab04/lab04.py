def skip_add(n):
    """ Takes a number n and returns n + n-2 + n-4 + n-6 + ... + 0.

    >>> skip_add(5)  # 5 + 3 + 1 + 0
    9
    >>> skip_add(10) # 10 + 8 + 6 + 4 + 2 + 0
    30
    >>> # Do not use while/for loops!
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(this_file, 'skip_add',
    ...       ['While', 'For'])
    True
    """
    "*** YOUR CODE HERE ***"
    if n <= 0:
        return 0
    else:
        return n + skip_add(n-2)

def summation(n, term):
    """Return the sum of the first n terms in the sequence defined by term.
    Implement using recursion!

    >>> summation(5, lambda x: x * x * x) # 1^3 + 2^3 + 3^3 + 4^3 + 5^3
    225
    >>> summation(9, lambda x: x + 1) # 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10
    54
    >>> summation(5, lambda x: 2**x) # 2^1 + 2^2 + 2^3 + 2^4 + 2^5
    62
    >>> # Do not use while/for loops!
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(this_file, 'summation',
    ...       ['While', 'For'])
    True
    """
    assert n >= 1
    "*** YOUR CODE HERE ***"
    
    if n == 1:
        return term(n)
    else:
        return term(n) + summation(n-1, term)

def paths(m, n):
    if m == 1 or n == 1:
        return 1
    else:
        return paths(m-1, n) + paths (m, n-1)

def max_subseq(n, t):    
    if n == 0 or t == 0:
        return 0
    with_ones = max_subseq(n//10, t-1) * 10 + n%10
    
    not_with = max_subseq(n//10, t)
    
    if with_ones > not_with:
        return with_ones
    else:
        return not_with

def add_chars(w1, w2):
    if len(w1) == 0:
        return ''
    elif w1[0] == w2[0]:
        return add_chars(w1[1:], w2[1:])
    elif w1[0] != w2[0]:
        return str(w2[0]) + add_chars(w1, w2[1:])